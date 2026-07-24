import os
import shutil

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.profiling_service import profile_dataset
from app.services.cleaning_service import clean_dataset
from app.services.insights_service import generate_insights




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
    # Read CSV
        df = pd.read_csv(file_path)

        # Clean dataset
        df = clean_dataset(df)

        # Generate business insights
        insights = generate_insights(df)

        # Profile dataset
        profile = profile_dataset(df)

        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "business_insights": insights,
            **profile
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV: {str(e)}"
        )