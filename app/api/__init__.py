from fastapi import APIRouter
from app.api.routes import usuarios, ganhos

router = APIRouter()
router.include_router(usuarios.router)
router.include_router(ganhos.router)
