from fastapi import APIRouter

from src.api.appointments import router as appointment_router
from src.api.auth import router as auth_router


router = APIRouter()

router.include_router(appointment_router, prefix="/tasks", tags=["tasks"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
