from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, FastAPI!"}

@app.get("/usuario/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
