from sqlalchemy.orm import Session
from sqlalchemy import update
from .utils import verificarObjeto
# Fazer um decorator para verificar se o objeto é None

class Repo():

    def __init__(self, db:Session, tabela) -> None:
        self.db = db
        self.tabela = tabela

    def dicio(self, obj):
        return obj.dict()

    def salvar(self, db_obj):
        # Salva as alterações no banco de dados
        self.db.commit()
        self.db.refresh(db_obj)

    def criar(self, obj):
        # Cria um objeto no banco de dados
        db_obj = self.tabela(**self.dicio(obj))
        self.db.add(db_obj)
        self.salvar(db_obj)
        return db_obj

    def listar(self):
        # Lista todos os objetos da tabela
        return self.db.query(self.tabela).all()
    
    @verificarObjeto
    def obter(self, id):
        # Obtem um objeto da tabela pelo o ID
        return self.db.query(self.tabela).filter(self.tabela.id == id).first()
        

    def remover(self, id):
        # Remove um objeto da tabela
        obj = self.obter(id) # Pode retornar um objeto ou None
        if obj: self.db.delete(obj); self.db.commit()
        return obj
    
    def editar(self, id, obj):
        update_stmt = update(self.tabela).where(
            self.tabela.id == id
        ).values(
            **obj.dict(exclude_unset=True)
        )
        self.db.execute(update_stmt)
        self.db.commit()
        return self.obter(id)
    
    def obterPrimeiro(self):
        return self.db.query(self.tabela).first()



        