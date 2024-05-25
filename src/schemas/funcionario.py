from datetime import date, datetime
from pydantic import BaseModel
from typing import ForwardRef, Optional, List

from .endereco import EnderecoSimples


class FuncionarioSimples(BaseModel):
    
    id : Optional[int]
    nome : str
    email : str
    admin : bool

    class Config:
        orm_mode = True


class Funcionario(BaseModel):
    
    id : Optional[int]

    nome: str
    dataNascimento: date

    telefone: str
    email: str
    instagram: str

    senha: str
    admin: bool
    porcentagemComissao: float = 50.0

    salao_id: int = 2

    endereco_id: Optional[int]
    endereco: Optional[EnderecoSimples]

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    email: str
    senha: str

    class Config:
        orm_mode = True

class LoginSucesso(BaseModel):
    token: str
    funcionario: FuncionarioSimples

    class Config:
        orm_mode = True