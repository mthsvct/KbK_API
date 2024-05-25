from sqlalchemy.orm import Session
from .repo import Repo
from .utils import verificarObjeto
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from src.infra.providers import hash_provider, token_provider
from fastapi import HTTPException


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
    

    def login(self, email:str, senha:str):
        f = self.obterEmail(email)

        if f is None:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado!")
        
        if not hash_provider.verificar_hash(senha, f.senha):
            raise HTTPException(status_code=401, detail="Senha incorreta!")

        token = token_provider.criar_access_token(
            {"sub": f.email}
        )
        
        return sc.LoginSucesso(token=token, funcionario=f)


