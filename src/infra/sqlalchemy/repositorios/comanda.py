from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repo import Repo
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from fastapi import HTTPException

from .cliente import Cliente

class Comanda(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Comanda)


    def criaObj(self, obj: md.Comanda):
        return md.Comanda(
            data=obj.data,
            dataFechamento=obj.dataFechamento,
            statusPagamento=obj.statusPagamento,
            valorTotal=obj.valorTotal,
            cliente_id=obj.cliente_id
        )    


    def criar(self, obj: sc.Comanda, ex=False):
        # Buscar o cliente
        cliente = Cliente(self.db).obter(obj.cliente_id)
        if cliente is None: # Se o cliente não existir, retornar um erro
            raise HTTPException(status_code=404,detail="Cliente não encontrado!")
        db_obj = self.criaObj(obj) # Criar o objeto
        self.salvar(db_obj)
        return sc.ComandaCliente(comanda=db_obj, cliente=cliente)

