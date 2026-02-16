from fastapi import APIRouter
from controllers.authController import login

router = APIRouter()

router.post('/token', response_model=dict)(login)