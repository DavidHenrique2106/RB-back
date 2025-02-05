import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("As variáveis SUPABASE_URL e SUPABASE_KEY não estão configuradas corretamente.")

# Criar cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str

@app.get("/usuarios/")
async def listar_usuarios():
    response = supabase.table("usuarios").select("*").execute()
    if response and response.data:
        return {"usuarios": response.data}
    raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")

@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    response = supabase.table("usuarios").insert(usuario.dict()).execute()
    if response and hasattr(response, "error") and response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário criado com sucesso", "usuario": response.data}

@app.put("/usuarios/{usuario_id}")
async def atualizar_usuario(usuario_id: int, usuario: Usuario):
    response = supabase.table("usuarios").update(usuario.dict()).eq("id", usuario_id).execute()
    if response and hasattr(response, "error") and response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/usuarios/{usuario_id}")
async def deletar_usuario(usuario_id: int):
    response = supabase.table("usuarios").delete().eq("id", usuario_id).execute()
    if response and hasattr(response, "error") and response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return {"message": "Usuário excluído com sucesso"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
