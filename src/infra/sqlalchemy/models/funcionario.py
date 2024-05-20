from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

# Apagar as tabelas: Pessoa, Contato

class Funcionario(Base):

    __tablename__ = 'funcionario'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)
    dataNascimento = Column(DateTime)

    telefone = Column(String)
    email = Column(String)
    instagram = Column(String)

    endereco_id = Column(Integer, ForeignKey('endereco.id'))
    endereco = relationship('Endereco', back_populates='funcionario')

    senha = Column(String)
    admin = Column(Boolean)
    porcentagemComissao = Column(Float)

    salao_id = Column(Integer, ForeignKey('salao.id', name='fk_funcionario_salao'))
    salao = relationship('Salao', back_populates='funcionario')

    atividade = relationship('Atividade', back_populates='funcionario')

    def __repr__(self):
        return f"<Funcionario: {self.nome}>"