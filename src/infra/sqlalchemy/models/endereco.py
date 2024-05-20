from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Endereco(Base):

    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, index=True)
    rua = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cep = Column(String)
    cidade = Column(String)
    estado = Column(String)
    complemento = Column(String)

    salao = relationship('Salao', back_populates='endereco')
    cliente = relationship('Cliente', back_populates='endereco')
    funcionario = relationship('Funcionario', back_populates='endereco')

    def __repr__(self): 
        return f"<Endereco: {self.rua} - {self.numero} - {self.cidade}>"

