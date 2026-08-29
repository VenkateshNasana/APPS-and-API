from fastapi import APIRouter
router = APIRouter()
@router.post('/simulate')
def simulate(): return {'status': 'ok'}
