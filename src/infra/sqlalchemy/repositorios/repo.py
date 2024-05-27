from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from .utils import verificarObjeto

class Repo():

    def __init__(self, db:Session, tabela) -> None:
        self.db = db
        self.tabela = tabela

    def dicio(self, obj, ex=False):
        # Transforma um objeto em um dicionário
        return obj.dict() if not ex else obj.dict(exclude_unset=True)

    def salvar(self, db_obj):
        # Salva as alterações no banco de dados
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)

    def criar(self, obj, ex=False):
        # Cria um objeto no banco de dados
        db_obj = self.tabela(**self.dicio(obj, ex=ex))
        self.salvar(db_obj)
        return db_obj

    def listar(self):
        # Lista todos os objetos da tabela
        return self.db.query(self.tabela).all()
    
    @verificarObjeto
    def obter(self, id):
        # Obtem um objeto da tabela pelo o ID
        return self.db.query(self.tabela).filter(self.tabela.id == id).first()
    
    @verificarObjeto
    def obterEmail(self, email):
        # Obtem um objeto da tabela pelo email
        return self.db.query(self.tabela).filter(self.tabela.email == email).first()    

    def remover(self, id):
        # Remove um objeto da tabela
        obj=self.obter(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Objeto não encontrado!")
        self.db.delete(obj)
        self.db.commit()
        return obj
    
    def editar(self, id, obj):
        # Edita um objeto da tabela
        if (instancia:=self.obter(id)) is None:
            raise HTTPException(status_code=404, detail="Objeto não encontrado!")
        update_stmt = update(self.tabela).where(self.tabela.id == id).values(**obj.dict(exclude_unset=True))
        self.db.execute(update_stmt)
        self.db.commit()
        return self.obter(id)
    
    def obterPrimeiro(self):
        # Obtem o primeiro objeto da tabela
        return self.db.query(self.tabela).first()