from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.ComandaSimples])
def listarComandas(f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Comanda(db).listar()


@router.get("/{id}", response_model=sc.Comanda)
def obterComanda(id:int, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    if (c:=rp.Comanda(db).obter(id)) is None:
        raise HTTPException(status_code=404, detail="Comanda não encontrada!")
    return c


@router.post("/", status_code=201, response_model=sc.ComandaCliente)
def criarComanda(c:sc.Comanda,f:sc.Funcionario=Depends(obter_usuario_logado),db:Session=Depends(get_db)):
    return rp.Comanda(db).criar(c)


@router.put("/{id}", response_model=sc.Comanda)
def editarComanda(id:int, c:sc.Comanda, f:sc.Funcionario=Depends(obter_usuario_logado), db:Session=Depends(get_db)):
    return rp.Comanda(db).editar(id, c)


@router.delete("/{id}", response_model=sc.Comanda)
def deleteComanda(
        id:int, 
        f:sc.Funcionario=Depends(obter_usuario_logado), 
        db:Session=Depends(get_db)
    ):
    return rp.Comanda(db).remover(id)




