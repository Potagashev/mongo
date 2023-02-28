from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from src.settings import get_database
from src.schemas import appointments as schemas


class AppointmentRepo:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)):
        self.db = db

    async def get_many(self):
        pass

    async def create(self, create_data: schemas.AppointmentCreate) -> schemas.AppointmentFull:
        new_student = await self.db["barbershop"]["appointments"].insert_one(create_data.dict())
        created_student = await self.db["barbershop"]["appointments"].find_one(
            {"_id": new_student.inserted_id}
        )
        print(dir(created_student))
        print(created_student)
        return created_student
