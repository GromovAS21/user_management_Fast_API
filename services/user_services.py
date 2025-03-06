import asyncio
from typing import Optional

from schemas.user import User, UserCreate

# Временная база данных для хранения пользователей
users_db = [
    {"id": 1, "name": "John", "age": 25, "email": "john@example.com"},
    {"id": 2, "name": "Jane", "age": 26, "email": "jane@example.com"},
]


async def fetch_users():
    """Получение списка пользователей"""
    await asyncio.sleep(1)  # имитация длительной операции
    return [User(**user) for user in users_db]


async def fetch_user(user_id: int) -> Optional[User]:
    """Получение пользователя по ID"""
    await asyncio.sleep(1)  # имитация длительной операции
    for user in users_db:
        if user.get("id") == user_id:
            return User(**user)
    return None


async def create_new_user(user_create: UserCreate) -> Optional[User]:
    """Создание нового пользователя"""
    await asyncio.sleep(1)  # имитация длительной операции
    list_users_id = []
    for user in users_db:
        list_users_id.append(user.get("id"))
        if user.get("email") == user_create.email:
            return None
    user_dict = user_create.model_dump()
    user_dict["id"] = max(list_users_id) + 1
    users_db.append(user_dict)
    return User(**user_dict)


async def delete_user(user_id: int) -> bool:
    """Удаление пользователя по ID"""
    await asyncio.sleep(1)  # имитация длительной операции
    for user in users_db:
        if user.get("id") == user_id:
            users_db.remove(user)
            return True
    return False
