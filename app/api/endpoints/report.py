from fastapi import APIRouter,UploadFile,File,Response
import os
import pandas as pd

router = APIRouter(prefix="/report", tags=["Report"])

@router.get("/summary")
def get_txt_file():
    file_path = os.path.join("artifacts","reports","model_summary.txt")
    with open(file_path, "r") as file:
        contents = file.read()

    return Response(content=contents, media_type="text/plain")

@router.get("/history")
def get_mosl_history():
    file_path = os.path.join("artifacts","reports","model_history")
    accuracy_df = pd.read_csv(os.path.join(file_path,"accuracy.csv"))
    loss_df = pd.read_csv(os.path.join(file_path,"loss.csv"))
    return {"accuarcy" :accuracy_df.to_dict(),"loss":loss_df.to_dict()}
