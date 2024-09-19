from fastapi import UploadFile
from typing import List
from app.services.YOLOtoPascalVOC import YOLOtoPascalVOC

def ConversionManager(files: List[UploadFile], convert_from: str, convert_to: str) -> List[UploadFile]:
	if (convert_from == "YOLO" and convert_to == "Pascal VOC"):
		return YOLOtoPascalVOC(files)
	return []
