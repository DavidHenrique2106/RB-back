from fastapi import APIRouter
from app.api.routes import usuarios

router = APIRouter()
router.include_router(usuarios.router)
