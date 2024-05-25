from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from src.infra.sqlalchemy.config.database import criar_bd
from src import schemas as sc

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy import repositorios as rp

from src.routers.salao import router as rt_salao
from src.routers.funcionario import router as rt_funcionario
from src.routers.cliente import router as rt_clientes

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

app.include_router(rt_salao, prefix="/salao")
app.include_router(rt_funcionario, prefix="/funcionarios")
app.include_router(rt_clientes, prefix="/clientes")
