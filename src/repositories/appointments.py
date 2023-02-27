from fastapi import Depends

from src.settings import db as mongo_db
from src.schemas import appointments as schemas


class AppointmentRepo:
    def __init__(self, db=Depends(mongo_db)):
        self.db = db

    async def get_many(self):
        pass

    async def create(self, create_data: schemas.AppointmentCreate) -> schemas.AppointmentFull:
        new_student = await self.db["appointments"].insert_one(create_data)
        created_student = await self.db["appointments"].find_one(
            {"_id": new_student.inserted_id}
        )
        print(dir(created_student))
        print(created_student)
        return created_student
