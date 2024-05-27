from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp


router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.AtividadeSimples])
def listarAtividades(
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Atividade(db).listar()


@router.get("/{id}", response_model=sc.Atividade)
def obterAtividade(
        id:int,
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    a = rp.Atividade(db).obter(id)
    if a is None:
        raise HTTPException(status_code=404, detail="Atividade não encontrada!")
    return a


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=sc.Atividade)
def criarAtividade(
        atividade:sc.Atividade,
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Atividade(db).criar(atividade, True)


@router.put("/{id}", response_model=sc.Atividade)
def editarAtividade(
        id:int, 
        atividade:sc.Atividade,
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Atividade(db).editar(id, atividade)


@router.delete("/{id}", response_model=sc.Atividade)
def deleteAtividade(
        id:int,
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Atividade(db).remover(id)
