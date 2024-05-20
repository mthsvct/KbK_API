from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Salao(Base):

    __tablename__ = 'salao'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    porcentagemComissao = Column(Float)

    telefone = Column(String)
    email = Column(String)
    instagram = Column(String)

    endereco_id = Column(Integer, ForeignKey('endereco.id'))
    endereco = relationship('Endereco', back_populates='salao')

    servico = relationship('Servico', back_populates='salao')
    
    funcionario = relationship('Funcionario', back_populates='salao')
    cliente = relationship('Cliente', back_populates='salao')

    def __repr__(self): 
        return f"<Salao: {self.nome}>"




