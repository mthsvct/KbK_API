from pydantic import BaseModel
from typing import ForwardRef, Optional, List
from datetime import datetime



class Pagamento(BaseModel):

    id: Optional[int]
    data: datetime
    valor: float
    forma: str

    comanda_id: int

    class Config:
        orm_mode = True