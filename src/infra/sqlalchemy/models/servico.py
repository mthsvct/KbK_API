from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Servico(Base):

    __tablename__ = 'servico'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    valorAPartir = Column(Float)
    duracao = Column(Integer)

    salao_id = Column(Integer, ForeignKey('salao.id', name='fk_servico_salao'))
    salao = relationship('Salao', back_populates='servico')

    atividade = relationship('Atividade', back_populates='servico')

    def __repr__(self):
        return f"<Servico: {self.nome}>"
