# https://www.alura.com.br/artigos/formatando-moeda-no-python
# https://alasco.tech/2020/01/31/handling-money-and-taxes-in-python.html
# https://docs.python.org/3/library/decimal.html
# https://docs.python.org/pt-br/3/library/datetime.html

# from ctypes import Union
from abc import ABC, abstractmethod
from decimal import Decimal
import datetime

class Operacao(ABC):

    def __init__(
            self, quantidade: int, valor_unitario: Decimal, liquidacao: Decimal,
            negociacao: Decimal, corretagem: Decimal, data: datetime) -> None:
        self._quantidade = quantidade
        self._valor_unitario = valor_unitario
        self._liquidacao = liquidacao
        self._negociacao = negociacao
        self._corretagem = corretagem
        self._data = data
        self._taxas = self._liquidacao + self._negociacao + self._corretagem
        self._valor_da_operacao = self.calcula_valor_da_operacao()
        self._preco_medio = self._valor/self._quantidade

    @abstractmethod
    def calcula_valor_da_operacao(self):
        pass

class Compra(Operacao):

    def calcula_valor_da_operacao(self):
        return self._valor_unitario*self._quantidade + self._taxas

class Venda(Operacao):

    def calcula_valor_da_operacao(self):
        return self._valor_unitario*self._quantidade - self._taxas

class Papel:

    # constructor
    def __init__(self, nome: str) -> None:
        self.__nome = nome.strip().upper()
        self.__quantidade = 0
        self.__lista_de_compras = []
        self.__lista_de_vendas = []
        #TODO: check if exists

    def _checar_existencia_do_papel(self) -> bool:
        pass

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


if __name__ == "__main__":

    prio3 = Papel("prio3")
    print(prio3)
