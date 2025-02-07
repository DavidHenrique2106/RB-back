from fastapi import APIRouter
from app.api.routes import usuarios, teste

router = APIRouter()
router.include_router(usuarios.router)
router.include_router(teste.router)
