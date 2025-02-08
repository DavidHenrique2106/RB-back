from fastapi import APIRouter, HTTPException
from app.services.usuario_service import UsuarioService
from app.schemas.usuario import UsuarioSchema
from uuid import UUID  

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/")
async def listar_usuarios():
    return UsuarioService.listar_usuarios()

@router.post("/cadastrar")
async def criar_usuario(usuario: UsuarioSchema):
    usuario_criado = UsuarioService.criar_usuario(usuario)
    if isinstance(usuario_criado, dict) and "mensagem" in usuario_criado:
        raise HTTPException(status_code=400, detail=usuario_criado["mensagem"])
    return usuario_criado

@router.put("/atualizar/{usuario_id}", response_model=UsuarioSchema)
async def atualizar_usuario(usuario_id: UUID, usuario: UsuarioSchema):
    usuario_atualizado = UsuarioService.atualizar_usuario(usuario_id, usuario)
    if isinstance(usuario_atualizado, dict) and "mensagem" in usuario_atualizado:
        raise HTTPException(status_code=404, detail=usuario_atualizado["mensagem"])
    return usuario_atualizado

@router.delete("/deletar/{usuario_id}", status_code=204)
async def excluir_usuario(usuario_id: UUID):
    sucesso = UsuarioService.excluir_usuario(usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário excluído com sucesso"}
