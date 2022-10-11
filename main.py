from abc import ABC, abstractmethod
from decimal import Decimal
import datetime


class Papel:

    # constructor
    def __init__(self, nome: str) -> None:
        self._nome = nome.strip().upper()
        self._lista_de_compras = []
        self._lista_de_vendas = []

    def _checar_existencia_do_papel(self) -> bool:
        pass

    def _quantidade_comprada(self) -> int:
        qtd = 0
        for compra in self._lista_de_compras:
            qtd += compra.quantidade
        return qtd

    def _quantidade_vendida(self) -> int:
        qtd = 0
        for venda in self._lista_de_vendas:
            qtd -= venda.quantidade
        return qtd

    def _valor_comprado(self) -> Decimal:
        valor = 0
        for compra in self._lista_de_compras:
            valor += compra.valor_da_operacao
        return valor

    def _valor_vendido(self) -> Decimal:
        valor = 0
        for venda in self._lista_de_vendas:
            valor += venda.valor_da_operacao
        return valor

    @property
    def quantidade(self) -> int:
        qtd = self._quantidade_comprada() - self._quantidade_vendida()
        return qtd

    @property
    def preco_medio(self) -> Decimal:
        preco = self._valor_comprado()/self._quantidade_comprada()
        return preco


class Operacao(ABC):

    def __init__(
            self, papel: Papel, quantidade: int, valor_unitario: Decimal, liquidacao: Decimal,
            negociacao: Decimal, corretagem: Decimal, data: datetime) -> None:
        self._papel = papel
        self._quantidade = quantidade   #TODO: check quantidade =/ 0
        self._valor_unitario = valor_unitario
        self._liquidacao = liquidacao
        self._negociacao = negociacao
        self._corretagem = corretagem
        self._data = data
        self._taxas = self._liquidacao + self._negociacao + self._corretagem
        self._valor_da_operacao = self.calcula_valor_da_operacao()
        self._preco_medio = self._valor_da_operacao/self._quantidade

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @property
    def valor_da_operacao(self) -> int:
        return self._valor_da_operacao

    @abstractmethod
    def calcula_valor_da_operacao(self):
        pass

    @abstractmethod
    def executa_operacao(self):
        pass

class Compra(Operacao):

    def calcula_valor_da_operacao(self):
        return self._valor_unitario*self._quantidade + self._taxas

    def executa_operacao(self):
        self._papel._lista_de_compras.append(self)
        return

class Venda(Operacao):

    def calcula_valor_da_operacao(self):
        return self._valor_unitario*self._quantidade - self._taxas

    def executa_operacao(self):
        self._papel._lista_de_vendas.append(self)
        return


if __name__ == "__main__":

    prio3 = Papel("prio3")
    print(prio3)
    a = Compra(prio3,10,Decimal("30.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    print(prio3._lista_de_compras)
    a.executa_operacao()
    print(prio3._lista_de_compras)
    print(prio3.quantidade)
    # b = Venda(prio3,5,Decimal("60.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    # b.executa_operacao()
    print(prio3.quantidade)
    print(prio3.preco_medio)
