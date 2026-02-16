from fastapi import APIRouter
from controllers.fileController import create_upload_file

router = APIRouter()

router.post('/upload/')(create_upload_file)