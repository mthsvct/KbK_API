from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base



class Cliente(Base):

    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    dataNascimento = Column(DateTime)

    telefone = Column(String)
    email = Column(String)
    instagram = Column(String)

    endereco_id = Column(Integer, ForeignKey('endereco.id'))
    endereco = relationship('Endereco', back_populates='cliente')

    salao_id = Column(Integer, ForeignKey('salao.id', name='fk_cliente_salao'))
    salao = relationship('Salao', back_populates='cliente')

    comanda = relationship('Comanda', back_populates='cliente')

    def __repr__(self):
        return f"<Cliente: {self.nome}>"
