from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    idade: int
