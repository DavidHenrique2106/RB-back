from fastapi import APIRouter, HTTPException
from app.services.usuario_service import UsuarioService
from app.schemas.usuario import UsuarioSchema

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/")
async def listar_usuarios():
    return UsuarioService.listar_usuarios()

@router.post("/")
async def criar_usuario(usuario: UsuarioSchema):
    return UsuarioService.criar_usuario(usuario)

@router.put("/{usuario_id}", response_model=UsuarioSchema)
async def atualizar_usuario(usuario_id: int, usuario: UsuarioSchema):
    usuario_atualizado = UsuarioService.atualizar_usuario(usuario_id, usuario)
    
    if not usuario_atualizado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return usuario_atualizado

@router.delete("/{usuario_id}", status_code=204)
async def excluir_usuario(usuario_id: int):
    sucesso = UsuarioService.excluir_usuario(usuario_id)
    
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return {"message": "Usuário excluído com sucesso"}
