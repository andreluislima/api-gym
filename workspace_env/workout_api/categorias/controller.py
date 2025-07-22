from fastapi import APIRouter, Body, status
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependecies import DatabaseDependency

router = APIRouter()

@router.post(
    path='/',
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def post(
    db_session: DatabaseDependency,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut: # type: ignore
    pass
