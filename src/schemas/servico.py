from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime


class Servico(BaseModel):

    id : Optional[int]
    nome: str
    descricao: str
    valorAPartir: float
    duracao: int

    salao_id : Optional[int] = 2

    class Config:
        orm_mode = True


class ServicoSimples(BaseModel):

    id : Optional[int]
    nome: str
    valorAPartir: float

    class Config:
        orm_mode = True