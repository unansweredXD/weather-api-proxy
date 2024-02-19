from fastapi import APIRouter
from router.weather import weather

router = APIRouter()
router.include_router(weather.router, tags=["Погода"], prefix="/weather")
