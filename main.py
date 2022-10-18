from abc import ABC, abstractmethod
from decimal import Decimal
import datetime


class Papel:

    # constructor
    def __init__(self, nome: str) -> None:
        self._nome = nome.strip().upper()
        self._quantidade = int(0)
        self._montante = Decimal("0")
        self._lista_de_compras = []
        self._lista_de_vendas = []

    def _checar_existencia_do_papel(self) -> bool:
        pass

    def _calcula_preco_medio(self) -> Decimal:
        if(self._quantidade > 0):
            return self._montante/self._quantidade
        return Decimal("0")

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @property
    def montante(self) -> int:
        return self._montante

    @property
    def preco_medio(self) -> Decimal:
        self._preco_medio = self._calcula_preco_medio()
        return round(self._preco_medio, 2)              # Esse é o melhor lugar para fazer o arredondamento?


class Operacao(ABC):

    def __init__(
            self, id_nota: str, data: datetime.date, papel: Papel, quantidade: int, valor_unitario: Decimal,
            liquidacao: Decimal, negociacao: Decimal, corretagem: Decimal, ISS: Decimal) -> None:
        self._id_nota = id_nota
        self._data = data
        self._papel = papel
        self._quantidade = quantidade
        self._valor_unitario = valor_unitario
        self._liquidacao = liquidacao
        self._negociacao = negociacao
        self._corretagem = corretagem
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
        self._papel._montante += self._valor_da_operacao
        self._papel._quantidade += self._quantidade
        self._papel._lista_de_compras.append(self)
        return

class Venda(Operacao):

    def calcula_valor_da_operacao(self):
        return self._valor_unitario*self._quantidade - self._taxas

    def executa_operacao(self):
        self._papel._montante *= (Decimal(1)-Decimal(self._quantidade)/Decimal(self._papel._quantidade))
        self._papel._quantidade -= self._quantidade
        self._papel._lista_de_vendas.append(self)
        return


class CalculadoraDeTaxas:

    def __init__(self, id_nota: int) -> None:
        pass


class Nota:

    def __init__(self, id_nota: int, data: datetime.date, taxas) -> None:
        pass


class LeitorDeNota:

    def __init__(self) -> None:
        pass


class LeitorDeDarf:

    def __init__(self) -> None:
        pass


if __name__ == "__main__":

    prio3 = Papel("prio3")
    a = Compra(prio3,10,Decimal("30.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    a.executa_operacao()
    print(prio3.preco_medio)
    print(prio3.quantidade)
    print(prio3.montante)
    b = Venda(prio3,5,Decimal("60.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    b.executa_operacao()
    print(prio3.preco_medio)
    print(prio3.quantidade)
    print(prio3.montante)
    c = Compra(prio3,100,Decimal("50.00"),Decimal("0"),Decimal("0"),Decimal("4.5"),30)
    c.executa_operacao()
    print(prio3.preco_medio)
    print(prio3.quantidade)
    print(prio3.montante)
