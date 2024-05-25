from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()


# --------------------------------- ROTAS --------------------------------- #


@router.get("/all", response_model=List[sc.FuncionarioSimples])
def listarFuncionarios(db:Session=Depends(get_db)):
    return rp.Funcionario(db).listar()


@router.get("/one/{id}", response_model=sc.Funcionario)
def obterFuncionario(id:int, db:Session=Depends(get_db)):
    f = rp.Funcionario(db).obter(id)
    if f is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado!")
    return f


@router.post("/cadastrar", status_code=201, response_model=sc.FuncionarioSimples)
def criarFuncionario(funcionario:sc.Funcionario, db:Session=Depends(get_db)):
    print("Passou aqui: f = ", funcionario)
    return rp.Funcionario(db).criar(funcionario)


@router.put("/{id}", response_model=sc.Funcionario)
def editarFuncionario(id:int, funcionario:sc.Funcionario, db:Session=Depends(get_db)):
    return rp.Funcionario(db).editar(id, funcionario)


@router.delete("/{id}", response_model=sc.Funcionario)
def deleteFuncionario(id:int, db:Session=Depends(get_db)):
    return rp.Funcionario(db).remover(id)


@router.post("/login", status_code=200)
def loginFuncionario(login:sc.LoginData, db:Session=Depends(get_db)):
    return rp.Funcionario(db).login(login.email, login.senha)


@router.get("/me", response_model=sc.FuncionarioSimples)
def me(funcionario:sc.Funcionario=Depends(obter_usuario_logado)):
    # Decodificar o token, pegar o telefone, buscar o user no bd e retornar
    return funcionario