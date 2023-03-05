import uuid

from fastapi import Depends
from passlib.handlers.bcrypt import bcrypt

from src import exceptions
from src.exceptions import ExceptionCode
from src.domain.users.repositories import UserRepo
from src.domain.users import schemas as schemas


class UserService:
    def __init__(self, repo: UserRepo = Depends(UserRepo)):
        self.repo = repo

    async def get_by_id(self, user_id: uuid.UUID) -> schemas.UserHashPw:
        user = await self.repo.get_by_id(user_id)
        if user:
            return user
        else:
            raise exceptions.NotFoundError(
                detail={
                    "msg": "The user with this ID was not found",
                    "code": ExceptionCode.user_with_id_not_found,
                },
            )

    async def get_by_email(self, email: str) -> schemas.UserHashPw:
        user = await self.repo.get_by_email(email)
        if user:
            return user
        else:
            raise exceptions.NotFoundError(
                detail={
                    "msg": "The user with this email was not found",
                    "code": ExceptionCode.user_with_email_not_found,
                },
            )

    async def register(
        self, user_data: schemas.UserCreate
    ) -> schemas.User:
        user = await self.repo.get_by_email(user_data.email)
        if user:
            raise exceptions.ConflictError(
                detail={
                    "msg": "Email must be unique. "
                    "User with this email already exists",
                    "code": ExceptionCode.user_already_exists,
                },
            )

        user_ = schemas.UserRepoCreate(
            **user_data.dict(exclude={"password"}),
            password_hash=bcrypt.hash(user_data.password)
        )
        return await self.repo.create(user_data=user_)

    async def change_password(
        self,
        user: schemas.UserHashPw,
        change_password_data: schemas.ChangePassword,
    ) -> schemas.User:
        old_password = change_password_data.old_password
        new_password = change_password_data.new_password

        if bcrypt.verify(secret=old_password, hash=user.password_hash):
            if old_password == new_password:
                raise exceptions.BadRequestError(
                    detail={
                        "msg": "The new password should not"
                        " be equal to the old one",
                        "code": ExceptionCode.old_pw_equal_to_new_pw,
                    },
                )

            return await self.repo.set_new_password(
                user_id=user.id, new_password_hash=bcrypt.hash(new_password)
            )
        else:
            raise exceptions.UnauthorizedError(
                detail={
                    "msg": "The password you passed is incorrect",
                    "code": ExceptionCode.incorrect_password,
                },
            )

    async def update_profile(
        self, user: schemas.User, update_profile_data: schemas.UserUpdate
    ) -> schemas.User:
        if update_profile_data.email != user.email and (
            await self.repo.get_by_email(email=update_profile_data.email)
        ):
            raise exceptions.ConflictError(
                detail={
                    "msg": "Email must be unique. "
                    "User with this email already exists",
                    "code": ExceptionCode.user_already_exists,
                },
            )
        return await self.repo.update_profile(user.id, update_profile_data)
