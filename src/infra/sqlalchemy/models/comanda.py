from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Comanda(Base):

    __tablename__ = 'comanda'

    id = Column(Integer, primary_key=True, index=True)
    
    data = Column(DateTime)
    statusPagamento = Column(String)
    valorTotal = Column(Float)

    cliente_id = Column(Integer, ForeignKey('cliente.id', name='fk_comanda_cliente'))
    cliente = relationship('Cliente', back_populates='comanda')

    atividade = relationship('Atividade', back_populates='comanda')
    pagamento = relationship('Pagamento', back_populates='comanda')

    def __repr__(self):
        return f"<Comanda: {self.id} - {self.cliente.nome}>"