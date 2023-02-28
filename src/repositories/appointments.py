import datetime

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from src.schemas.common import PyObjectId
from src.settings import get_database
from src.schemas import appointments as schemas


class AppointmentRepo:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)):
        self.db = db

    async def get_many(self) -> list[schemas.AppointmentFull]:
        appointments = await self.db["barbershop"]["appointments"].find().to_list(100)
        print(appointments)
        return appointments

    async def create(self, create_data: schemas.AppointmentCreate) -> schemas.AppointmentFull:
        create_data_dict = create_data.dict()
        create_data_dict['created_at'] = datetime.datetime.now()
        new_appointment = await self.db["barbershop"]["appointments"].insert_one(create_data_dict)
        return await self.get_by_id(new_appointment.inserted_id)

    async def get_by_id(self, appointment_id: PyObjectId) -> schemas.AppointmentFull:
        return await self.db["barbershop"]["appointments"].find_one(
            {"_id": appointment_id}
        )
