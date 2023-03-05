import os

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import MongoDsn


class Settings:
    mongo_dsn: MongoDsn = os.environ.get("MONGODB_URL")
    jwt_secret: str = os.environ.get("JWT_SECRET")
    jwt_algorithm: str = "HS256"
    auth_token_expire: int = 36000
    pw_reset_token_expire: int = 300
    database_name: str = "barbershop"
    appointments_collection: str = "appointments"


db = AsyncIOMotorClient(Settings.mongo_dsn)


async def get_database() -> AsyncIOMotorClient:
    return db


database_name = "barbershop"
appointments_collection = "appointments"
