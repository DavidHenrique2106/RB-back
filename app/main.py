import os
import uvicorn
from fastapi import FastAPI
from app.api import router
from app.core.config import settings

app = FastAPI(
    title="Swagger com FastAPI",
    description="Documentação automática com Swagger",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def home():
    return {"message": "API rodando na Render 🚀"}

if __name__ == "__main__":
    print(f"Iniciando servidor na porta {settings.PORT}...")
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
