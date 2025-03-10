from typing import List

from fastapi import APIRouter, HTTPException, Depends

from schemas.user import User, UserCreate
from services.jwt_token_services import verify_jwt_token
from services.user_services import fetch_users, fetch_user, create_new_user, delete_user

router = APIRouter()

@router.get("/")
async def read_root():
    """Запрос к корню проекта"""
    return {"massage": ", User Management World!"}

@router.get("/users/", response_model=List[User])
async def get_users():
    """Получение списка пользователей"""
    return await fetch_users()


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Получение пользователя по ID"""
    user = await fetch_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    """Создание пользователя"""
    user = await create_new_user(user)
    if user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return user


@router.delete("/users/{user_id}")
async def delete_user_route(user_id: int):
    """Удаление пользователя"""
    user = await delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

@router.get("/protected")
async def protected_route(user_id: int = Depends(verify_jwt_token)):
    """Закрытый маршрут"""
    return {"message": f"Hello, user {user_id}"}
