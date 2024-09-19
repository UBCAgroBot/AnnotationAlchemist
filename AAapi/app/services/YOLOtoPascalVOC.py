"""
For experimenting with conversions.	
"""
from fastapi import UploadFile
from typing import List

def YOLOtoPascalVOC(upload_files: List[UploadFile]) -> List[UploadFile]:
	if len(upload_files) == 0:
		return []

	upload_txts= _FilterNonTextFiles(upload_files)

	for upload_txt in upload_txts:
		with upload_txt.file as f:
			for line in f:
				line = line.decode("utf-8").strip()
				print(line)

	return []

def _FilterNonTextFiles(files: List[UploadFile]) -> List[UploadFile]:
	"""
	Only allow files that end in .txt
	"""
	for upload_file in files:
		file_name = upload_file.filename;
		if not file_name:
			files.remove(upload_file)
			continue
		if not file_name.endswith('.txt'):
			files.remove(upload_file)
			
	return files

