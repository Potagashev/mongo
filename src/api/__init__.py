from fastapi import APIRouter

from src.api.appointments import router as appointment_router

router = APIRouter()

router.include_router(appointment_router, prefix="/tasks", tags=["tasks"])
