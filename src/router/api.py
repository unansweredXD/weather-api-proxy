from fastapi import APIRouter

from router.router import router

api_router = APIRouter(prefix="/api")
api_router.include_router(router)
