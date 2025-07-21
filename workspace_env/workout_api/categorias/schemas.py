
from workspace_env.workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class Categoria(BaseSchema):
    nome:Annotated[str, Field(description='Nome da Categoria', max_length=10)]
    