from datetime import datetime

from pydantic import BaseModel

from src.schemas.common import PyObjectId


class AppointmentBase(BaseModel):
    master_name: str
    client_name: str
    date_time: datetime


class AppointmentFull(AppointmentBase):
    id: PyObjectId


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(AppointmentBase):
    pass
