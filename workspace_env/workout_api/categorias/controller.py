from uuid import UUID
from fastapi import APIRouter, Body, status
from sqlalchemy import select
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependecies import DatabaseDependency
from workout_api.categorias.models import CategoriaModel
from fastapi import HTTPException

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
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out
    
    
@router.get(
    path='/',
    summary='Consultar todas as categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut]
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:  # type: ignore
    
    # categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all() # type: ignore
    
    result = await db_session.execute(select(CategoriaModel))
    categorias_model = result.scalars().all()
    categorias_out = [CategoriaOut.model_validate(categoria) for categoria in categorias_model]
    
    return categorias_out   
    
@router.get(
    path='/{id}',
    summary='Consultar categoria pelo Id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut
)
async def query(id: UUID, db_session: DatabaseDependency) -> CategoriaOut:  # type: ignore
    
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first() # type: ignore
    
    if not categoria:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada para o id {id}'
        )
    
    return categoria