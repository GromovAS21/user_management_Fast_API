from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

def create_jwt_token(data: dict):
    """Создание токена"""
    to_encode = data.copy()
    expire = datetime.now() + timedelta(days=1)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_jwt_token(data = {"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
