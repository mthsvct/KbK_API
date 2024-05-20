from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime

from .atividade import Atividade
from .pagamento import Pagamento


class ComandaSimples(BaseModel):
    
    id : Optional[int]
    data : datetime
    statusPagamento: str
    valorTotal: float = 0.0

    class Config:
        orm_mode = True


class Comanda(BaseModel):
    id : Optional[int]
    data : datetime
    statusPagamento: str
    valorTotal: float = 0.0

    cliente_id : int

    atividade: Optional[List[Atividade]]
    pagamento: Optional[Pagamento]  

    class Config:
        orm_mode = True




