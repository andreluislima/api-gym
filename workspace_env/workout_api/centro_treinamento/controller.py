from uuid import UUID, uuid4
from fastapi import APIRouter, Body, status
from sqlalchemy import select
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependecies import DatabaseDependency
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from fastapi import HTTPException

router = APIRouter()

@router.post(
    path='/',
    summary='Criar novo Centro de Treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut
)
async def post(
    db_session: DatabaseDependency,
    CentroTreinamentoIn: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut: # type: ignore
    
    centroTreinamentoOut = CentroTreinamentoOut(id=uuid4(), **CentroTreinamentoIn.model_dump())
    centroTreinamentoModel = CentroTreinamentoModel(**centroTreinamentoOut.model_dump())
    
    db_session.add(centroTreinamentoModel)
    await db_session.commit()
    
    return centroTreinamentoOut
    
    
@router.get(
    path='/',
    summary='Consultar todas os Centros de Treinamento',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut]
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:  # type: ignore
    
    # categorias: list[CentroTreinamentoOut] = (await db_session.execute(select(CategoriaModel))).scalars().all() # type: ignore
    
    result = await db_session.execute(select(CentroTreinamentoModel))
    centroTreinamentoModel = result.scalars().all()
    centroTreinamentoOut = [CentroTreinamentoOut.model_validate(categoria) for categoria in centroTreinamentoModel]
    
    return centroTreinamentoOut   
    
@router.get(
    path='/{id}',
    summary='Consultar Centro de Treinamento pelo Id',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut
)
async def query(id: UUID, db_session: DatabaseDependency) -> CentroTreinamentoOut:  # type: ignore
    
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first() # type: ignore
    
    if not centro_treinamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'CT não encontrado para o id {id}'
        )
    
    return centro_treinamento