from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime


class Salario(BaseModel):

    id: Optional[int]
    valor: float
    qntAtividades : int
    qntDiasTrabalhados : int
    dataInicio : datetime
    dataFim : datetime
    funcionario_id : int

    class Config:
        orm_mode = True