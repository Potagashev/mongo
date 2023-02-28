from datetime import datetime

from pydantic import BaseModel

from src.schemas.common import PyObjectId


class AppointmentBase(BaseModel):
    master_name: str
    client_name: str


class AppointmentFull(AppointmentBase):
    id: PyObjectId
    date_time: datetime


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(AppointmentBase):
    pass
