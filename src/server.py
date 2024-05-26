from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.salao import router as rt_salao
from src.routers.funcionario import router as rt_funcionario
from src.routers.cliente import router as rt_clientes
from src.routers.servico import router as rt_servico
from src.routers.comanda import router as rt_comandas
from src.routers.atividade import router as rt_atividades

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
app.include_router(rt_clientes, prefix="/clientes")
app.include_router(rt_funcionario, prefix="/funcionarios")
app.include_router(rt_salao, prefix="/salao")
app.include_router(rt_servico, prefix="/servicos")
app.include_router(rt_comandas, prefix="/comandas")
app.include_router(rt_atividades, prefix="/atividades")
