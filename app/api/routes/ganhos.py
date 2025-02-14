from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.services.ganhos_service import GanhosServices
from app.schemas.ganhos import ValoresSchema, ValoresResponseSchema

router = APIRouter(prefix="/ganhos", tags=["Ganhos"])

@router.get("/", response_model=list[ValoresResponseSchema])
async def listar_ganhos():
    return GanhosServices.listar_ganhos()

@router.post("/enviar", response_model=ValoresResponseSchema)
async def mandar_ganhos(ganho: ValoresSchema):
    ganho_adicionado = GanhosServices.mandar_ganhos(ganho)  
    
    if "mensagem" in ganho_adicionado:
        raise HTTPException(status_code=400, detail=ganho_adicionado["mensagem"])  
    
    return ganho_adicionado

@router.put("/atualizar/{ganho_id}", response_model=ValoresResponseSchema)
async def atualizar_ganhos(ganho_id: int, ganho: ValoresSchema):
    ganho_atualizado = GanhosServices.atualizar_ganhos(ganho_id, ganho)
    
    if isinstance(ganho_atualizado, dict) and "mensagem" in ganho_atualizado:
        raise HTTPException(status_code=404, detail=ganho_atualizado["mensagem"])
    
    return ganho_atualizado

@router.delete("/deletar/{ganho_id}", status_code=204)
async def deletar_ganho(ganho_id: int):
    sucesso = GanhosServices.deletar_ganho(ganho_id)
    
    if not sucesso:
        raise HTTPException(status_code=404, detail="Ganho não encontrado")
    
    return {"message": "Ganho deletado com sucesso"}
