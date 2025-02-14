from app.schemas.ganhos import ValoresSchema, ValoresResponseSchema
from app.models.ganhos import GanhosModels  
from app.core.database import supabase
from uuid import UUID
from datetime import datetime

class GanhosServices:
    @staticmethod
    def listar_ganhos():
        response = supabase.table(GanhosModels.TABLE_NAME).select("*").execute()
        return response.data or []  

    @staticmethod
    def mandar_ganhos(ganho: ValoresSchema):
        response = supabase.table(GanhosModels.TABLE_NAME).insert({
            "descricao": ganho.descricao,
            "valor": ganho.valor,
            "criado_em": ganho.criado_em.isoformat()  
        }).execute()
        
        return response.data[0] if response.data else {"mensagem": "Erro ao enviar ganhos"}

    @staticmethod
    def atualizar_ganhos(ganho_id: UUID, ganho: ValoresSchema):
        response = supabase.table(GanhosModels.TABLE_NAME).update({
            "descricao": ganho.descricao,
            "valor": ganho.valor,
            "criado_em": ganho.criado_em.isoformat()
        }).eq("id", str(ganho_id)).execute()

        if not response.data:
            return {"mensagem": "Ganho não encontrado ou erro ao atualizar"}

        return response.data[0]

    @staticmethod
    def deletar_ganho(ganho_id: UUID):
        response = supabase.table(GanhosModels.TABLE_NAME).delete().eq("id", str(ganho_id)).execute()

        if not response.data:
            return False  

        return True
