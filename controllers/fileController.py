from fastapi import APIRouter, UploadFile, File as UploadFileType
from services.fileService import upload_file

router = APIRouter()

@router.post('/upload/')
async def create_upload_file(file: UploadFileType = UploadFile(...)):
    return await upload_file(file)