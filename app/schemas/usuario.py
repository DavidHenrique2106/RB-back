from pydantic import BaseModel, EmailStr
from uuid import UUID

class UsuarioSchema(BaseModel):
    id: UUID | None = None 
    nome: str
    email: EmailStr
    senha: str
