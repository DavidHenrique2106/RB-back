from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ValoresSchema(BaseModel):
    descricao: str = Field(..., min_length=3, max_length=255, description="Descrição do gasto")
    valor: float = Field(..., gt=0, description="Valor do gasto, deve ser maior que zero")
    criado_em: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Data de criação")

class ValoresResponseSchema(ValoresSchema):
    id: int = Field(..., description="ID do gasto no banco de dados")
