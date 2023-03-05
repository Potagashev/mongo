from pydantic import BaseModel, EmailStr, Field

from src.domain.common.schemas import PyObjectId


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    biography: Field(max_length=200)

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass


class UserCreate(UserBase):
    password: str


class UserRepoCreate(UserBase):
    password_hash: str


class User(UserBase):
    id: PyObjectId
    is_admin: bool


class UserHashPw(User):
    password_hash: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str


class EmailModel(BaseModel):
    email: EmailStr
