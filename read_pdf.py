from datetime import date
from decimal import Decimal
from PyPDF2 import PdfReader
from click import FileError
from numpy import quantile

fname = "000991087_SPOT_FORWARD_20221014_N002608650.pdf"

reader = PdfReader(fname)

number_of_pages = len(reader.pages)
if (number_of_pages != 1):
    raise NotImplementedError(
        "Verificar número de páginas da nota de corretagem."
    )

page = reader.pages[0]

text = page.extract_text()

if (text.splitlines(True)[0].strip().upper() != "NOTA DE CORRETAGEM"):
    raise FileError("Arquivo incorreto, não é uma nota de corretagem.")

id_nota = text.splitlines(True)[1].split()[0]

data_lida = text.splitlines(True)[3].split()[0].split(sep="/")
data = date(int(data_lida[-1]), int(data_lida[-2]), int(data_lida[0]))

#Loop enquanto linha começar com 1-BOVESPA?
linha = text.splitlines(True)[26].split()
kind = "compra" if linha[1] == "CVISTA" else "venda"
papel = linha[2]
quantidade = int(linha[3])
preco_unitario = Decimal(linha[4])

#nova linha será o número da última acima + x, no caso atual:
liquidacao = Decimal(text.splitlines(True)[38].split()[0].replace(",", "."))
emolumentos = Decimal(text.splitlines(True)[44].split()[0].replace(",", "."))
