from fastapi import Depends

from src.repositories.appointments import AppointmentRepo
from src.schemas import appointments as schemas


class AppointmentService:
    def __init__(self, repo: AppointmentRepo = Depends(AppointmentRepo)):
        self.repo = repo

    async def get_many(self) -> list[schemas.AppointmentFull]:
        return await self.repo.get_many()

    async def create(
        self, create_data: schemas.AppointmentCreate
    ) -> schemas.AppointmentFull:
        return await self.repo.create(create_data)
