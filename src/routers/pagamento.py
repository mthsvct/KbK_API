from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.Pagamento])
def listar(f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Pagamento(db).listar()

@router.get("/{id}", response_model=sc.Pagamento)
def obter(id: int, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    obj = rp.Pagamento(db).obter(id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Objeto não encontrado!")
    return obj


@router.post("/", status_code=201, response_model=sc.Pagamento)
def criar(obj: sc.Pagamento, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Pagamento(db).criar(obj)


@router.put("/{id}", response_model=sc.Pagamento)
def editar(id: int, obj: sc.Pagamento, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Pagamento(db).editar(id, obj)


@router.delete("/{id}", response_model=sc.Pagamento)
def delete(id: int, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Pagamento(db).remover(id)
