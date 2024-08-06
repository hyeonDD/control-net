from fastapi import APIRouter

from backend_app.api.endpoints import start_game, evaluation_model

api_router = APIRouter()
api_router.include_router(
    start_game.router, prefix="/sketch-image", tags=["images"])

api_router.include_router(
    evaluation_model.router, prefix="/test-model", tags=["test"])
