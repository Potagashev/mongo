from datetime import datetime

from pydantic import BaseModel

from src.domain.common.schemas import Declarative, PyObjectId
from src.domain.users import schemas as user_schemas


class AppointmentBase(BaseModel):
    customer_name: str
    date_time: datetime
    comment: str


class AppointmentFull(AppointmentBase, Declarative):
    master: user_schemas.User
    is_confirmed: bool


class AppointmentCreate(AppointmentBase):
    master_id: PyObjectId


class AppointmentUpdate(AppointmentBase):
    pass
