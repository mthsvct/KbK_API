from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime

from .cliente import Cliente

from .atividade import Atividade, AtividadeSimples, AtividadeSimplesSrv
from .pagamento import Pagamento


class ComandaSimples(BaseModel):

    id : Optional[int]
    data : datetime
    dataFechamento: Optional[datetime] = None
    statusPagamento: Optional[str] = "PENDENTE" # PENDENTE, PAGO, PARCIAL
    valorTotal: Optional[float] = 0.0
    cliente_id : Optional[int]
    
    pago: Optional[float] = 0.0 # Valor pago
    faltante: Optional[float] = 0.0 # Valor pago
    
    class Config:
        orm_mode = True


class ComandaSimplesAtv(BaseModel):

    id : Optional[int]
    data : datetime
    dataFechamento: Optional[datetime] = None
    statusPagamento: Optional[str] = "PENDENTE" # PENDENTE, PAGO, PARCIAL
    valorTotal: Optional[float] = 0.0
    cliente_id : Optional[int]
    
    pago: Optional[float] = 0.0 # Valor pago
    faltante: Optional[float] = 0.0 # Valor pago

    atividade: Optional[List[AtividadeSimplesSrv]] = []
    
    class Config:
        orm_mode = True

class Comanda(BaseModel):

    id : Optional[int]
    data : datetime
    dataFechamento: Optional[datetime] = None
    statusPagamento: Optional[str] = "PENDENTE" # PENDENTE, PAGO, PARCIAL
    valorTotal: Optional[float] = 0.0
    cliente_id : Optional[int]
    cliente: Optional[Cliente]
    
    pago: Optional[float] = 0.0 # Valor pago
    faltante: Optional[float] = 0.0 # Valor pago

    atividade: Optional[List[AtividadeSimples]] = []
    pagamento: Optional[List[Pagamento]] = []
    
    class Config:
        orm_mode = True


