import os
import json
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline

router = APIRouter(prefix="/predict", tags=["Predict"])


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@router.post("/")
def predict_route(image: dict):
    try:
        clApp = ClientApp()
        image_data = image.get("image")
        decodeImage(image_data, clApp.filename)
        result = clApp.classifier.predict()
    except Exception as e:
        return HTTPException(status_code=500, detail="Something Went wrong")
    return JSONResponse(content=result)
