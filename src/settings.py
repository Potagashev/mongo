import os

from motor.motor_asyncio import AsyncIOMotorClient

db = AsyncIOMotorClient(os.environ.get("MONGODB_URL"))


async def get_database() -> AsyncIOMotorClient:
    return db


database_name = "barbershop"
appointments_collection = "appointments"
