from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Pagamento(Base):

    __tablename__ = 'pagamento'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime)
    valor = Column(Float)
    forma = Column(String)

    comanda_id = Column(Integer, ForeignKey('comanda.id', name='fk_pagamento_comanda'))
    comanda = relationship('Comanda', back_populates='pagamento')

    def __repr__(self):
        return f"<Pagamento: {self.id} - {self.comanda.id}>"