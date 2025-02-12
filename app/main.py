import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.api import router
from app.core.config import settings

app = FastAPI(
    title="Swagger com FastAPI",
    description="Documentação automática com Swagger",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
async def home():
    return {"message": "API rodando na Render 🚀"}

if __name__ == "__main__":
    print(f"Iniciando servidor na porta {settings.PORT}...")
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
