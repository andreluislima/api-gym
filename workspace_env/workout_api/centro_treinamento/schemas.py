
from workspace_env.workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class CentroTreinamento(BaseSchema):
    nome:Annotated[str, Field(description='CT King', max_length=10)]
    endereco:Annotated[str, Field(description='Endereço do CT', max_length=60)]
    propietario:Annotated[str, Field(description='Propietario do CT', max_length=30)]
