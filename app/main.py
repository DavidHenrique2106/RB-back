from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str

@app.get("/usuarios/")
async def listar_usuarios():
    response = supabase.table("usuarios").select("*").execute()
    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return response.data

@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    response = supabase.table("usuarios").insert(usuario.dict()).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário criado com sucesso", "usuario": response.data}

@app.put("/usuarios/{usuario_id}")
async def atualizar_usuario(usuario_id: int, usuario: Usuario):
    response = supabase.table("usuarios").update(usuario.dict()).eq("id", usuario_id).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/usuarios/{usuario_id}")
async def deletar_usuario(usuario_id: int):
    response = supabase.table("usuarios").delete().eq("id", usuario_id).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário excluído com sucesso"}
