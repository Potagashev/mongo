from fastapi import APIRouter, Depends

from src.schemas import appointments as schemas
from src.services.appointments import AppointmentService

router = APIRouter()


@router.get("", response_model=list[schemas.AppointmentFull])
async def get_appointments(
    service: AppointmentService = Depends(),
) -> list[schemas.AppointmentFull]:
    return await service.get_many()


@router.post("", response_model=schemas.AppointmentFull)
async def create_appointment(
    create_data: schemas.AppointmentCreate, service: AppointmentService = Depends()
) -> schemas.AppointmentFull:
    return await service.create(create_data)
