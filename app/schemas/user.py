from pydantic import BaseModel, EmailStr
from app.utils.security import hash_password

class UserBase(BaseModel):
    username: str
    full_name: str = None
    email: str = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str = None


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

