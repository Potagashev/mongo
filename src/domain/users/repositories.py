import uuid

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.users import schemas as schemas
from src.settings import get_database


class UserRepo:
    def __init__(self, database: AsyncIOMotorClient = Depends(get_database)):
        self.database = database

    async def create(self, user_data: schemas.UserRepoCreate) -> schemas.User:
        pass

    async def get_by_id(
        self, user_id: uuid.UUID
    ) -> schemas.UserHashPw | None:
        pass

    async def get_by_email(self, email: str) -> schemas.UserHashPw | None:
        pass

    async def set_new_password(
        self, user_id: uuid.UUID, new_password_hash: str
    ) -> schemas.User | None:
        pass

    async def update_profile(
        self, user_id: uuid.UUID, update_profile_data: schemas.UserUpdate
    ) -> schemas.User | None:
        pass

    async def delete(self, user_id: uuid.UUID):
        pass
