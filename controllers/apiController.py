from fastapi import APIRouter

router = APIRouter()

@router.get('/api')
async def api_root():
    return {'message': 'API root'}