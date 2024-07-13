from pydantic import Field, PositiveFloat
from typing import Annotated, Optional
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centros_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Atleta", example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", example='12345678910', max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=90.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", example=1.90)]
    sexo: Annotated[str, Field(description="Sexo do Atleta", example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do Atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de Treinamento do Atleta")]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do Atleta", example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade do Atleta", example=25)]