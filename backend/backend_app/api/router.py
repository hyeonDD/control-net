from fastapi import APIRouter

from backend_app.api.endpoints import get_image

api_router = APIRouter()
api_router.include_router(get_image.router, prefix="/image", tags=["images"])
