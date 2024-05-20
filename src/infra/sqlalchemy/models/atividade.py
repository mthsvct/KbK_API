from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Atividade(Base):

    __tablename__ = 'atividade'

    id = Column(Integer, primary_key=True, index=True)

    preco = Column(Float)
    
    comanda_id = Column(Integer, ForeignKey('comanda.id', name='fk_atividade_comanda'))
    comanda = relationship('Comanda', back_populates='atividade')

    funcionario_id = Column(Integer, ForeignKey('funcionario.id', name='fk_atividade_funcionario'))
    funcionario = relationship('Funcionario', back_populates='atividade')

    servico_id = Column(Integer, ForeignKey('servico.id', name='fk_atividade_servico'))
    servico = relationship('Servico', back_populates='atividade')

    def __repr__(self):
        return f"<Atividade: {self.id} - {self.comanda.id} - {self.funcionario.pessoa.nome}>"