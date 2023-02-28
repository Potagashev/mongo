from datetime import datetime

from pydantic import BaseModel

from src.schemas.common import PyObjectId, Declarative


class AppointmentBase(BaseModel):
    master_name: str
    client_name: str
    date_time: datetime


class AppointmentFull(AppointmentBase, Declarative):
    pass


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(AppointmentCreate):
    pass
