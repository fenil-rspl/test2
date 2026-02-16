from fastapi import APIRouter
from controllers.userController import read_user

router = APIRouter()

router.get('/users/{user_id}', response_model=dict)(read_user)