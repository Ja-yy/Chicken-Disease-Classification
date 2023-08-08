import os
import json
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/train", tags=["Train"])


@router.get("/")
def train_route():
    try:
        os.system("dvc repro")
    except Exception as e:
        return HTTPException(status_code=500, detail="Something Went wrong")
    return JSONResponse({"message": "Training done successfully!"}, status_code=200)
