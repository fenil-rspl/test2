from fastapi import APIRouter, Depends
from models import User
from services.userService import get_user

router = APIRouter()

@router.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user