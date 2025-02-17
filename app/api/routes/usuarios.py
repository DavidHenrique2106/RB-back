from fastapi import APIRouter, HTTPException, Depends
from app.services.usuario_service import UsuarioService
from app.schemas.usuario import UsuarioSchema, LoginSchema
from app.core.auth import verificar_token
from uuid import UUID  
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/")
async def listar_usuarios(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    usuarios = UsuarioService.listar_usuarios()
    return usuarios
    
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario_logado = UsuarioService.autenticar_usuario(form_data.username, form_data.password)
    if not usuario_logado:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"access_token": usuario_logado["token"], "token_type": "bearer"}

@router.post("/cadastrar")
async def criar_usuario(usuario: UsuarioSchema):
    usuario_criado = UsuarioService.criar_usuario(usuario)
    if isinstance(usuario_criado, dict) and "mensagem" in usuario_criado:
        raise HTTPException(status_code=400, detail=usuario_criado["mensagem"])
    return usuario_criado

@router.put("/atualizar/{usuario_id}")
async def atualizar_usuario(usuario_id: UUID, usuario: UsuarioSchema, token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    usuario_atualizado = UsuarioService.atualizar_usuario(usuario_id, usuario)
    if not usuario_atualizado or (isinstance(usuario_atualizado, dict) and "mensagem" in usuario_atualizado):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario_atualizado

@router.delete("/deletar/{usuario_id}", status_code=204)
async def excluir_usuario(usuario_id: UUID, token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    sucesso = UsuarioService.excluir_usuario(usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário excluído com sucesso"}
