from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src import schemas as sc
from typing import List
from src.infra.sqlalchemy import repositorios as rp

router = APIRouter()




@router.get("/salao", response_model=sc.Salao)
def listarSalao(db:Session=Depends(get_db)):
    return rp.Salao(db).obterPrimeiro()


@router.post("/salao", status_code=status.HTTP_201_CREATED, response_model=sc.Salao)
def criarSalao(salao: sc.Salao, db:Session=Depends(get_db)):
    return rp.Salao(db).criar(salao)




