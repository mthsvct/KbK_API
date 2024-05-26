from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime

from .atividade import Atividade
from .pagamento import Pagamento


class ComandaSimples(BaseModel):

    id : Optional[int]
    data : datetime
    statusPagamento: Optional[str] = "PENDENTE" # PENDENTE, PAGO, PARCIAL
    valorTotal: Optional[float] = 0.0
    cliente_id : Optional[int]
    
    class Config:
        orm_mode = True


class Comanda(BaseModel):

    id : Optional[int]
    data : datetime
    dataFechamento: Optional[datetime] = None
    statusPagamento: Optional[str] = "PENDENTE" # PENDENTE, PAGO, PARCIAL
    valorTotal: Optional[float] = 0.0
    cliente_id : Optional[int]
    atividade: Optional[List[Atividade]] = []
    pagamento: Optional[List[Pagamento]] = []
    
    class Config:
        orm_mode = True


