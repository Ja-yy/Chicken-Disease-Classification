from fastapi import APIRouter
from app.api.endpoints import predicts
from app.api.endpoints import report

router = APIRouter(prefix="/api/v1")


router.include_router(predicts.router)
router.include_router(report.router)