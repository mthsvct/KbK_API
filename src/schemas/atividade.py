from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime

from .funcionario import Funcionario, FuncionarioSimples
from .servico import Servico



class AtividadeSimples(BaseModel):

    id : Optional[int]
    preco : float
    comanda_id : int
    funcionario_id : int
    servico_id : int
    
    class Config: orm_mode = True


class AtividadeSimplesSrv(BaseModel):

    id : Optional[int]
    preco : float
    comanda_id : int
    funcionario_id : int
    servico_id : int
    
    servico : Optional[Servico]
    
    class Config: orm_mode = True


class Atividade(BaseModel):

    id : Optional[int]
    preco : float
    comanda_id : int
    funcionario_id : int
    funcionario : Optional[FuncionarioSimples]
    servico_id : int
    servico : Optional[Servico]

    class Config: orm_mode = True
    