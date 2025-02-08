from app.schemas.usuario import UsuarioSchema, LoginSchema
from app.core.database import supabase
from uuid import UUID

class UsuarioService:
    @staticmethod
    def listar_usuarios():
        response = supabase.table("usuarios").select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def criar_usuario(usuario: UsuarioSchema):
        response = supabase.table("usuarios").insert({
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha
        }).execute()
        if response.data:
            return response.data[0]  
        return {"mensagem": "Erro ao criar usuário"}

    @staticmethod
    def atualizar_usuario(usuario_id: UUID, usuario: UsuarioSchema):
        response = supabase.table("usuarios").update({
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha
        }).eq("id", usuario_id).execute()
        return response.data if response.data else {"mensagem": "Usuário não encontrado"}

    @staticmethod
    def excluir_usuario(usuario_id: UUID):
        response = supabase.table("usuarios").delete().eq("id", usuario_id).execute()
        return response.status_code == 204

    @staticmethod
    def autenticar_usuario(email: str, senha: str):
        response = supabase.table("usuarios").select("*").eq("email", email).execute()
        if response.data:
            usuario = response.data[0]
            if usuario['senha'] == senha: 
                return {"id": usuario['id'], "nome": usuario['nome'], "email": usuario['email']}
        return None
