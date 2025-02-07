from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/teste", tags=["Teste"])

class Item(BaseModel):
    nome: str

@router.post("/enviar")
async def receber_nome(item: Item):
    return {"mensagem": f"Recebido com sucesso: {item.nome}"}
