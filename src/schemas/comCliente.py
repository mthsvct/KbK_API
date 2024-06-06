from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime

from .atividade import Atividade
from .pagamento import Pagamento
from .cliente import Cliente, ClienteSimples
from .comanda import ComandaSimples, Comanda, ComandaSimplesAtv



class ComandaCliente(BaseModel):
    
    comanda: ComandaSimples
    cliente: ClienteSimples
    
    class Config:
        orm_mode = True


class ComandaClienteATV(BaseModel):
    
    comanda: ComandaSimplesAtv
    cliente: ClienteSimples
    
    class Config:
        orm_mode = True


class ComandasCli(BaseModel):
    
    cliente: ClienteSimples
    comandas: List[ComandaSimples]
    
    class Config:
        orm_mode = True


class AbertasFechadas(BaseModel):
    abertas: List[ComandaClienteATV]
    fechadas: List[ComandaClienteATV]
    
    class Config:
        orm_mode = True