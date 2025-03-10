from fastapi import FastAPI

from middleware import LogMiddleware
from routers import user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

app.add_middleware(LogMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
