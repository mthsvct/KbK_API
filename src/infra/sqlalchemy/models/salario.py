from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Salario(Base):

    __tablename__ = 'salario'

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, default=0.0)
    qntAtividades = Column(Integer, default=0)
    qntDiasTrabalhados = Column(Integer, default=0)
    dataInicio = Column(DateTime, default=None)
    dataFim = Column(DateTime, default=None)
    funcionario_id = Column(Integer, ForeignKey('funcionario.id', name='fk_salario_funcionario'))
    funcionario = relationship('Funcionario', back_populates='salario')

    def __repr__(self):
        return f"<Salario: {self.id} - {self.funcionario.pessoa.nome} - {self.valor}>"