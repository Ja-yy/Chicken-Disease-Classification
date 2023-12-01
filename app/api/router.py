from fastapi import APIRouter
from app.api.endpoints import predicts


router = APIRouter(prefix="/api/v1")


router.include_router(predicts.router)
