from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do Atleta',max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta',max_length=11)]
    idade: Annotated[str, Field(description='Idade do Atleta')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta')]
    genero: Annotated[str, Field(description='Gênero do Atleta', max_length=1)]