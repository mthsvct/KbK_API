from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from src.infra.sqlalchemy.config.database import criar_bd
from src import schemas as sc

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy import repositorios as rp

from src.routers.salao import router as salao_router


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------- ROTAS ---------------------------- #

app.include_router(salao_router)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/endereco", status_code=status.HTTP_201_CREATED, response_model=sc.Endereco)
# def criar_endereco(endereco: sc.Endereco, db: Session = Depends(get_db)):
#     return rp.Endereco(db).criar(endereco)

# @app.post("/salao", status_code=status.HTTP_201_CREATED, response_model=sc.Salao)
# def criar_salao(salao: sc.Salao, db: Session = Depends(get_db)):
#     print('\n\n', salao, '\n\n')
#     return rp.Salao(db).criar(salao)

# @app.post(
#     "/funcionario/cadastrar", 
#     status_code=status.HTTP_201_CREATED, 
#     response_model=sc.Funcionario)
# def cadastrar_funcionario(funcionario: sc.Funcionario, db:Session = Depends(get_db)):
#     return rp.Funcionario(db).criar(funcionario)


# alembic init alembic