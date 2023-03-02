import datetime

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_obj_as

from src.domain.appointments import schemas as schemas
from src.domain.common.schemas import PyObjectId
from src.settings import get_database, Settings


class AppointmentRepo:
    def __init__(self, db: AsyncIOMotorClient = Depends(get_database)):
        self.db = db

    async def get_by_id_or_none(self, id: PyObjectId) -> schemas.AppointmentFull | None:
        appointment = await self.db[Settings.database_name][Settings.appointments_collection].find_one(
            {"_id": id}
        )
        return schemas.AppointmentFull.parse_obj(appointment)

    async def get_many(self, user_id: PyObjectId) -> list[schemas.AppointmentFull]:
        appointments = (
            await self.db[Settings.database_name][Settings.appointments_collection].find().to_list(100)
        )
        return parse_obj_as(list[schemas.AppointmentFull], appointments)

    async def create(
        self, create_data: schemas.AppointmentCreate
    ) -> schemas.AppointmentFull:
        create_data_dict = create_data.dict()
        create_data_dict["created_at"] = datetime.datetime.now()
        new_appointment = await self.db[Settings.database_name][
            Settings.appointments_collection
        ].insert_one(create_data_dict)
        return await self.get_by_id_or_none(new_appointment.inserted_id)

    async def update(self, id: PyObjectId, data: schemas.AppointmentUpdate) -> schemas.AppointmentFull:
        pass

    async def delete(self, id: PyObjectId) -> schemas.AppointmentFull:
        pass
