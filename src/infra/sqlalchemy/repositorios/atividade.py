from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from .utils import verificarObjeto
from src.infra.sqlalchemy.repositorios.repo import Repo
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from .comanda import Comanda


class Atividade(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Atividade)

    def atualizarValor(self, id):
        Comanda(self.db).atualizarValor(id)
    
    def criar(self, obj, ex=False):
        aux = super().criar(obj, ex)
        self.atualizarValor(aux.comanda_id)
        return aux
    
    def editar(self, id, obj):
        instancia = super().editar(id, obj)
        self.atualizarValor(instancia.comanda_id)
        return instancia

    def remover(self, id):
        # Obter o objeto com todas as relações necessárias carregadas
        obj = self.db.query(self.tabela).options(
            joinedload(self.tabela.servico),
            joinedload(self.tabela.funcionario)
        ).filter(self.tabela.id == id).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Objeto não encontrado!")
        self.db.delete(obj)
        self.db.commit()
        self.atualizarValor(obj.comanda_id)
        return obj


