from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    token: str


class SignInForm(BaseModel):
    email: EmailStr
    password: str
