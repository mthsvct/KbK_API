from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repo import Repo
from src import schemas as sc
from src.infra.sqlalchemy import models as md


class Endereco(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Endereco)