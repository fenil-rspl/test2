from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.authService import authenticate_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    return {'access_token': user.username, 'token_type': 'bearer'}