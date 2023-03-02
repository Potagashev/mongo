from fastapi import Depends

from src import exceptions
from src.domain.appointments.repositories import AppointmentRepo
from src.domain.appointments import schemas as schemas
from src.domain.common.schemas import PyObjectId
from src.domain.users import schemas as user_schemas


class AppointmentService:
    def __init__(self, repo: AppointmentRepo = Depends()):
        self.repo = repo

    async def get_by_id(self, id: PyObjectId, user: user_schemas.User) -> schemas.AppointmentFull:
        await self._check_access(id, user)
        appointment = await self.repo.get_by_id_or_none(id)
        return appointment

    async def get_many(self, user: user_schemas.User) -> list[schemas.AppointmentFull]:
        return await self.repo.get_many(user.id)

    async def create(
        self, data: schemas.AppointmentCreate, user: user_schemas.User
    ) -> schemas.AppointmentFull:
        data = schemas.AppointmentCreate(**data.dict(), master_id=user.id)
        return await self.repo.create(data)

    async def update(
        self, id: PyObjectId, data: schemas.AppointmentUpdate, user: user_schemas.User
    ) -> schemas.AppointmentFull:
        await self._check_access(id, user)
        return await self.repo.update(id, data)

    async def delete(
        self, id: PyObjectId, user: user_schemas.User
    ):
        await self._check_access(id, user)
        return await self.repo.delete(id)

    async def _check_access(self, id, user):
        appointment = await self.repo.get_by_id_or_none(id)
        if appointment:
            if appointment.master.id != user and not user.is_admin:
                raise exceptions.ForbiddenError()
        else:
            raise exceptions.NotFoundError()
