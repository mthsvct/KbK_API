from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.ClienteSimples])
def listarClientes(
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Cliente(db).listar()


@router.get("/{id}", response_model=sc.Cliente)
def obterCliente(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    c = rp.Cliente(db).obter(id)
    if c is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return c


@router.post("/cadastrar", status_code=201, response_model=sc.ClienteSimples)
def criarCliente(
        cliente:sc.Cliente,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Cliente(db).criar(cliente, ex=True)


@router.put("/{id}", response_model=sc.Cliente)
def editarCliente(
        id:int, 
        cliente:sc.Cliente,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Cliente(db).editar(id, cliente)


@router.delete("/{id}", response_model=sc.Cliente)
def deleteCliente(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Cliente(db).remover(id)