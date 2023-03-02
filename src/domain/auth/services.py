import uuid
from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt

from src import exceptions
from src.exceptions import ExceptionCode
from src.domain.users.schemas import UserHashPw
from src.domain.auth.schemas import Token
from src.domain.users.services import UserService
from src.settings import Settings

oauth2_auth_token = OAuth2PasswordBearer(tokenUrl="/auth/sign-in-swagger")


class AuthService:
    def __init__(
        self,
        user_service: UserService = Depends(UserService),
        settings: Settings = Depends(Settings),
    ):
        self.settings = settings
        self.user_service = user_service

    async def validate_token(self, token: str) -> UserHashPw:
        try:
            payload = jwt.decode(
                token,
                self.settings.jwt_secret,
                algorithms=[self.settings.jwt_algorithm],
            )
        except JWTError:
            raise exceptions.UnauthorizedError(
                detail={
                    "msg": "The authentication token you provided is "
                    "invalid",
                    "code": ExceptionCode.invalid_auth_token,
                },
            )
        user_id = payload.get("id")
        return await self.user_service.get_by_id(user_id)

    def create_token(self, user_id: uuid.UUID) -> Token:
        now = datetime.utcnow()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=self.settings.auth_token_expire),
            "id": str(user_id),
        }
        token = jwt.encode(
            payload,
            self.settings.jwt_secret,
            algorithm=self.settings.jwt_algorithm,
        )
        return Token(token=token)

    async def authenticate_user(self, email: str, password: str) -> Token:
        user = await self.user_service.get_by_email(email=email)
        if bcrypt.verify(secret=password, hash=user.password_hash):
            return self.create_token(user.id)
        else:
            raise exceptions.UnauthorizedError(
                detail={
                    "msg": "Incorrect email or password",
                    "code": ExceptionCode.incorrect_creds,
                },
            )
