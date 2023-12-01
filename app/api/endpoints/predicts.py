from fastapi import APIRouter,UploadFile,File
from cnnClassifier.pipeline.predict import PredictionPipeline


router = APIRouter(prefix="/predict", tags=["Predict"])

@router.post("/")
async def predict_route(img: UploadFile = File(...)):
    image_bytes = await img.read()
    classifier  = PredictionPipeline(image_bytes)
    ret = classifier.predict()
    print("=-=-=-=-=-=-ret",ret)
    return {"name":img.filename,"content_type":img.content_type,"prediction":ret[0].get("image")}