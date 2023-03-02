import uuid

from fastapi import APIRouter, Depends

from src import responses
from src.api.utils import get_current_user
from src.domain.appointments import schemas as schemas
from src.domain.users.schemas import User
from src.domain.appointments.services import AppointmentService

router = APIRouter()


@router.get(
    "/{id}",
    response_model=schemas.AppointmentFull,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: {"model": responses.UserWithIdNotFoundModel},
    },
)
async def get_by_id(
    id: uuid.UUID,
    service: AppointmentService = Depends(),
    user: User = Depends(get_current_user),
) -> schemas.AppointmentFull:
    return await service.get_by_id(id, user)


@router.get(
    "",
    response_model=list[schemas.AppointmentFull],
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: {"model": responses.UserWithIdNotFoundModel},
    },
)
async def get_many(
    service: AppointmentService = Depends(),
    user: User = Depends(get_current_user),
) -> list[schemas.AppointmentFull]:
    return await service.get_many(user)


@router.post(
    "",
    response_model=schemas.AppointmentFull,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: {"model": responses.UserWithIdNotFoundModel},
    },
)
async def create(
    create_data: schemas.AppointmentCreate,
    service: AppointmentService = Depends(),
    user: User = Depends(get_current_user),
) -> schemas.AppointmentFull:
    return await service.create(create_data, user)


@router.put(
    "/{id}",
    response_model=schemas.AppointmentFull,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: {"model": responses.UserWithIdNotFoundModel},
    },
)
async def update(
    id: uuid.UUID,
    update_data: schemas.AppointmentUpdate,
    service: AppointmentService = Depends(),
    user: User = Depends(get_current_user),
) -> schemas.AppointmentFull:
    return await service.update(id, update_data, user)


@router.delete(
    "/{id}",
    status_code=204,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: APPOINTMENT_AND_USER_NOT_FOUND_RESPONSES,
    },
)
async def delete(
    id: uuid.UUID,
    create_data: schemas.AppointmentUpdate,
    service: AppointmentService = Depends(),
    user: User = Depends(get_current_user),
) -> schemas.AppointmentFull:
    return await service.delete(id, create_data, user)
