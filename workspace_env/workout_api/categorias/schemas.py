
from workout_api.contrib.schemas import BaseSchema
from pydantic import UUID4, Field
from typing import Annotated

class CategoriaIn(BaseSchema):
    nome:Annotated[str, Field(description='Nome da Categoria', max_length=30)]
    

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]

    