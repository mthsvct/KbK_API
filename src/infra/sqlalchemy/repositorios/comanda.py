from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repo import Repo
from src import schemas as sc
from src.infra.sqlalchemy import models as md
from fastapi import HTTPException

from .cliente import Cliente

class Comanda(Repo):

    def __init__(self, db: Session) -> None:
        super().__init__(db, md.Comanda)

    
    def atualizarValor(self, id):
        obj = self.obter(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Objeto não encontrado!")
        atvs = self.db.query(md.Atividade).filter(md.Atividade.comanda_id == id).all()
        valorTotal = sum([atv.preco for atv in atvs])
        obj.valorTotal = valorTotal
        self.db.commit()
        return obj


    def criaObj(self, obj: md.Comanda):
        return md.Comanda(
            data=obj.data,
            dataFechamento=obj.dataFechamento,
            statusPagamento=obj.statusPagamento,
            valorTotal=obj.valorTotal,
            cliente_id=obj.cliente_id
        )    


    def criar(self, obj: sc.Comanda, ex=False):
        # Buscar o cliente
        cliente = Cliente(self.db).obter(obj.cliente_id)
        if cliente is None: # Se o cliente não existir, retornar um erro
            raise HTTPException(status_code=404,detail="Cliente não encontrado!")
        db_obj = self.criaObj(obj) # Criar o objeto
        self.salvar(db_obj)
        return sc.ComandaCliente(comanda=db_obj, cliente=cliente)
    

    def valores(self, comanda):
        pagamentos = self.db.query(md.Pagamento).filter(md.Pagamento.comanda_id == comanda.id).all()
        pago = sum([p.valor for p in pagamentos])
        faltante = comanda.valorTotal - pago
        return pago, faltante
    
    def obter(self, id):
        comanda = super().obter(id)
        if comanda is None:
            return None
        pago, faltante = self.valores(comanda)
        comanda.pago = pago
        comanda.faltante = faltante
        return comanda


    def listar(self):
        # Lista todos os objetos da tabela
        lista = self.db.query(md.Comanda).all()
        nLista = []
        for c in lista:
            novo = sc.Comanda(**c.__dict__)
            pago, faltante = self.valores(c)
            novo.pago = pago
            novo.faltante = faltante
            nLista.append(novo)
        return nLista

