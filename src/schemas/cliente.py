from pydantic import BaseModel
from typing import ForwardRef, Optional, List

from .endereco import EnderecoSimples
from .comanda import ComandaSimples



class ClienteSimples(BaseModel):
        
    id : Optional[int]
    nome : str
    email : str

    class Config:
        orm_mode = True


class Cliente(BaseModel):

    id: Optional[int]
    
    nome: str
    dataNascimento: str

    telefone: str
    email: str
    instagram: str

    salao_id : int = 2
    endereco_id : Optional[int]
    
    comanda: Optional[List[ComandaSimples]]
    endereco: Optional[EnderecoSimples]

    class Config:
        orm_mode = True