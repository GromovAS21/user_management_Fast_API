from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """Схема для пользователя"""
    id: int
    name: str
    age: int = Field(ge=0, title="Age")
    email: EmailStr

class UserCreate(BaseModel):
    """Схема для создания пользователя"""
    name: str
    age: int = Field(ge=0, title="Age")
    email: EmailStr