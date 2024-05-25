from sqlalchemy.orm import Session
from .repo import Repo
from .utils import verificarObjeto
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from src.infra.providers import hash_provider



class Funcionario(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Funcionario)

    @verificarObjeto
    def obterEmail(self, email):
        return self.db.query(md.Funcionario).filter(md.Funcionario.email == email).first()

    def criar(self, obj):
        # Verifica se o funcionario já não existe
        f = self.obterEmail(obj.email)
        if f is None: 
            print(obj.senha)
            obj.senha = hash_provider.gerar_hash(obj.senha)
            f = super().criar(obj)
        return f

