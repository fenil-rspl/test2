import shutil
from fastapi import UploadFile
from config.constants import UPLOAD_DIRECTORY

async def upload_file(file: UploadFile):
    file_location = f'{UPLOAD_DIRECTORY}/{file.filename}'
    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'info': f'file '{file.filename}' saved at '{file_location}''}