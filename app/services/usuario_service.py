from uuid import UUID
from passlib.context import CryptContext
from app.schemas.usuario import UsuarioSchema
from app.core.database import supabase
from app.core.auth import criar_token_jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService:
    @staticmethod
    def listar_usuarios():
        response = supabase.table("usuarios").select("*").execute()
        return response.data or []

    @staticmethod
    def criar_usuario(usuario: UsuarioSchema):
        senha_hash = pwd_context.hash(usuario.senha)
        response = supabase.table("usuarios").insert({
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": senha_hash
        }).execute()
        return response.data[0] if response.data else {"mensagem": "Erro ao criar usuário"}

    @staticmethod
    def atualizar_usuario(usuario_id: UUID, usuario: UsuarioSchema):
        senha_hash = pwd_context.hash(usuario.senha)
        response = supabase.table("usuarios").update({
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": senha_hash
        }).eq("id", usuario_id).execute()
        return response.data or {"mensagem": "Usuário não encontrado"}

    @staticmethod
    def excluir_usuario(usuario_id: UUID):
        response = supabase.table("usuarios").delete().eq("id", usuario_id).execute()
        return response.status_code == 204

    @staticmethod
    def autenticar_usuario(email: str, senha: str):
        response = supabase.table("usuarios").select("*").eq("email", email).execute()
        
        if not response.data:
            return None
        
        usuario = response.data[0]
        
        if not pwd_context.verify(senha, usuario["senha"]):
            return None
        
        token = criar_token_jwt({"id": usuario["id"], "nome": usuario["nome"], "email": usuario["email"]})
        
        return {"usuario": usuario, "token": token}
