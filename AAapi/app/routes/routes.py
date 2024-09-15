from fastapi import APIRouter, File, UploadFile
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def home():
    return "Hello, I am the AAapi 🧙"

@router.post("/api/upload-folder")
async def upload_folder(files: List[UploadFile] = File(...)):
    # Process the files
    for file in files:
        print("Got file: " + file.filename)

    return JSONResponse(content={"message": "Files uploaded successfully!"})
