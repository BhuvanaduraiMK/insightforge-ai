import os
import shutil

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile

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
        df = pd.read_csv(file_path)
        rows, columns = df.shape
        missing_values = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()
        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "rows": rows,
            "columns_count": columns,
            "missing_values": int(missing_values),
            "duplicate_rows": int(duplicate_rows),
            "columns": list(df.columns),
            "preview": df.head().to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV: {str(e)}"
        )