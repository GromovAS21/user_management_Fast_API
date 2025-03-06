from fastapi import FastAPI

from routers import user

app = FastAPI()

app.include_router(user.router)


@app.get("/")
async def read_root():
    """Запрос к корню проекта"""
    return {"massage": ", User Management World!"}
