from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.Salario])
def listarSalarios(
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salario(db).listar()


@router.get("/{id}", response_model=sc.Salario)
def obterSalario(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    s = rp.Salario(db).obter(id)
    if s is None:
        raise HTTPException(status_code=404, detail="Salario não encontrado!")
    return s


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=sc.Salario)
def criarSalario(
        slr:sc.Salario,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salario(db).criar(slr, True)


@router.put("/{id}", response_model=sc.Salario)
def editarSalario(
        id:int,
        slr:sc.Salario,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salario(db).editar(id, slr)


@router.delete("/{id}", response_model=sc.Salario)
def deleteSalario(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salario(db).remover(id)


@router.get("/funcionario/{idFuncionario}")
def obterSalarioFuncionario(
        idFuncionario:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salario(db).obterSalarioFuncionario(idFuncionario)