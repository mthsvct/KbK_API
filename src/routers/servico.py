from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()

# --------------------------------- ROTAS --------------------------------- #

@router.get("/all", response_model=List[sc.ServicoSimples])
def listarServicos(
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Servico(db).listar()


@router.get("/{id}", response_model=sc.Servico)
def obterServico(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    s = rp.Servico(db).obter(id)
    if s is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado!")
    return s


@router.post("/cadastrar", status_code=201, response_model=sc.ServicoSimples)
def criarServico(
        servico:sc.Servico,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Servico(db).criar(servico)


@router.put("/{id}", response_model=sc.Servico)
def editarServico(
        id:int, 
        servico:sc.Servico,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Servico(db).editar(id, servico)


@router.delete("/{id}", response_model=sc.Servico)
def deleteServico(
        id:int,
        f:sc.Funcionario=Depends(obter_usuario_logado),
        db:Session=Depends(get_db)
    ):
    return rp.Servico(db).remover(id)
