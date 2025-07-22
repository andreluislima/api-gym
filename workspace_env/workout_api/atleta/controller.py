from fastapi import APIRouter, Body, status
from workout_api.atleta.schemas import AtletaIn
from workout_api.contrib.dependecies import DatabaseDependency


router = APIRouter()

@router.post(
            path='/',
            summary='Criar novo atleta',
            status_code=status.HTTP_201_CREATED             
)
async def post(
            db_session: DatabaseDependency, 
            atleta_insert: AtletaIn = Body()):
    pass