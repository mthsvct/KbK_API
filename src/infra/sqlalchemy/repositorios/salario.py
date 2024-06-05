from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repo import Repo
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from .funcionario import Funcionario
from fastapi import HTTPException

class Salario(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Salario)

    def obterSalarioFuncionario(self, idFuncionario:int):
        funcionario = Funcionario(self.db).obter(idFuncionario)
        if not funcionario:
            raise HTTPException(status_code=404,detail="Funcionário não encontrado")
        salarios = self.db.query(self.tabela).filter(self.tabela.funcionario_id==idFuncionario).all()
        # Ordenar salários por data de início
        salarios = sorted(salarios, key=lambda x: x.dataInicio)
        salarios.reverse()
        return salarios