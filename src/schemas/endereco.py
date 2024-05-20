from pydantic import BaseModel
from typing import Optional


class EnderecoSimples(BaseModel):
        
    id : Optional[int]
    rua : str
    numero : str
    cidade : str

    class Config:
        orm_mode = True



class Endereco(BaseModel):

    id : Optional[int]
    rua : str
    numero : str
    bairro : str
    cep : str
    cidade : str
    estado : str
    complemento : str

    class Config:
        orm_mode = True