from pydantic import BaseModel
from typing import ForwardRef, Optional, List

from .servico import ServicoSimples
from .endereco import EnderecoSimples


class SalaoSimples(BaseModel):
        
    id: Optional[int]
    nome: str
    porcentagemComissao: float
    
    class Config:
        orm_mode = True


class Salao(BaseModel):
    
    id: Optional[int]
    nome: str
    porcentagemComissao: Optional[float] = 50.0

    telefone: str
    email: str
    instagram: str
    
    endereco_id: Optional[int]
    endereco: Optional[EnderecoSimples]

    servico: Optional[List[ServicoSimples]]

    
    class Config:
        orm_mode = True


ForwardRef('SalaoSimples')
