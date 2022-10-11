# https://www.alura.com.br/artigos/formatando-moeda-no-python
# https://alasco.tech/2020/01/31/handling-money-and-taxes-in-python.html
# https://docs.python.org/3/library/decimal.html
# https://docs.python.org/pt-br/3/library/datetime.html

# from ctypes import Union
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

    @property
    def quantidade(self) -> int:
        qtd = 0
        for compra in self._lista_de_compras:
            print(compra)
            qtd += compra.quantidade
        for venda in self._lista_de_vendas:
            qtd -= venda.quantidade
        return qtd


    # def compra(
    #         self, quantidade: int, valor_unitario: str, liquidacao: Union[str,Decimal], negociacao: Union[str,Decimal],
    #         corretagem: Union[str,Decimal], data: datetime) -> None:

    #     self.__quantidade += quantidade
    #     valor = Decimal(str(valor_unitario))

    #     #negociacao 0,0050%
    #     #liquidacao 0,0250%
    #     # if automaticamente_calculado:
    #     #     flag revisar taxas!


    # def vende(self, quantidade: int) -> None:
    #     self.__quantidade -= quantidade

    #lista de operaçoes compra e venda


class Operacao(ABC):

    def __init__(
            self, papel: Papel, quantidade: int, valor_unitario: Decimal, liquidacao: Decimal,
            negociacao: Decimal, corretagem: Decimal, data: datetime) -> None:
        self._papel = papel
        self._quantidade = quantidade
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
    b = Venda(prio3,3,Decimal("30.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    b.executa_operacao()
    print(prio3.quantidade)
