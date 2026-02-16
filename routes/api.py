from fastapi import APIRouter
from controllers.apiController import api_root

router = APIRouter()

router.get('/api')(api_root)