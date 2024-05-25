from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()




@router.get("/", response_model=sc.Salao)
def listarSalao(
        funcionario:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Salao(db).obterPrimeiro()


@router.post("/salao", status_code=status.HTTP_201_CREATED, response_model=sc.Salao)
def criarSalao(
        salao: sc.Salao,
        funcionario:sc.Funcionario=Depends(obter_usuario_logado), 
        db:Session=Depends(get_db)
    ):
    return rp.Salao(db).criar(salao)




