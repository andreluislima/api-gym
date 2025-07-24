from pydantic import Field, PositiveFloat
from typing import Annotated, Optional

from workout_api.contrib.schemas import BaseSchema,OutMixIn
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta',max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta',max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta')]
    genero: Annotated[str, Field(description='Gênero do Atleta', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do Atleta')]
    centro_treinamento: Annotated [CentroTreinamentoAtleta, Field(description='Centro de Treinamento do Atleta')]    
    
    
class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixIn):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta',max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do Atleta')]
