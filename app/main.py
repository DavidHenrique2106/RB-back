import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

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
    return {"message": "API funcionando!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    print(f"Iniciando servidor na porta {port}")  
    uvicorn.run(app, host="0.0.0.0", port=port)
