
from workout_api.contrib.schemas import BaseSchema
from pydantic import UUID4, Field
from typing import Annotated

class CentroTreinamento(BaseSchema):
    nome:Annotated[str, Field(description='CT King', max_length=10)]
    endereco:Annotated[str, Field(description='Endereço do CT', max_length=60)]
    propietario:Annotated[str, Field(description='Propietario do CT', max_length=30)]

class CentroTreinamentoIn(BaseSchema):
    nome:Annotated[str, Field(description='Nome do Centro de Treinamento', max_length=10)]
    

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador da Centro de Treinamento')]