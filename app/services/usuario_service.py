from app.schemas.usuario import UsuarioSchema

class UsuarioService:
    def __init__(self):
        self.usuarios = [
            {"id": 1, "nome": "João", "email": "joao@example.com", "idade": 25},
            {"id": 2, "nome": "Maria", "email": "maria@example.com", "idade": 30},
        ]
    
    def listar_usuarios(self):
        return self.usuarios

    def criar_usuario(self, usuario: UsuarioSchema):
        novo_usuario = {"id": len(self.usuarios) + 1, "nome": usuario.nome, "email": usuario.email, "idade": usuario.idade}
        self.usuarios.append(novo_usuario)
        return novo_usuario
    
    def atualizar_usuario(self, usuario_id: int, usuario: UsuarioSchema):
        usuario_encontrado = next((u for u in self.usuarios if u["id"] == usuario_id), None)
        
        if usuario_encontrado:
            usuario_encontrado["nome"] = usuario.nome
            usuario_encontrado["email"] = usuario.email
            usuario_encontrado["idade"] = usuario.idade
            return usuario_encontrado
        return None
    
    def excluir_usuario(self, usuario_id: int):
        usuario_encontrado = next((u for u in self.usuarios if u["id"] == usuario_id), None)
        
        if usuario_encontrado:
            self.usuarios.remove(usuario_encontrado)
            return True
        return False
