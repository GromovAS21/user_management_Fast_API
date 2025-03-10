from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """Схема для пользователя"""
    id: int
    name: str
    age: int
    email: EmailStr

class UserCreate(BaseModel):
    """Схема для создания пользователя"""
    name: str = Field(min_length=1, max_length=50, title="Name")
    age: int = Field(ge=0, le=120, title="Age")
    email: EmailStr