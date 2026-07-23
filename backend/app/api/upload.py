import os
import shutil

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.profiling_service import profile_dataset

router = APIRouter(
    prefix="/upload",
    tags=["File Upload"]
)

UPLOAD_FOLDER = "uploads"


@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:
        profile = profile_dataset(file_path)
        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            **profile
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV: {str(e)}"
        )