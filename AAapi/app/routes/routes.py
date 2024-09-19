from fastapi import APIRouter, File, Form, UploadFile
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def home():
	return "Hello, I am the AAapi 🧙"

@router.post("/api/upload-folder")
async def upload_folder(
	files: List[UploadFile] = File(...),
	convert_from: str = Form(...),
	convert_to: str = Form(...)
):
	"""
	Receives a JS FormData object as a message body
	"""
	# Process the files
	print("Convert from:" + convert_from)
	print("Convert to:" + convert_to)
	for file in files:
		print("Got file: " + file.filename)

	return JSONResponse(content={"data": "Files uploaded successfully!", "error":None})
