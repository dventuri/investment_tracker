import numpy as np
from decimal import Decimal

lista_operacoes = [Decimal(957.20), Decimal(1080.00), Decimal(98.32)]
taxas = Decimal(0.11)
total = 2135.52

sum = 0
completo = []
rounded = []
for operacao in lista_operacoes:
    parcial = operacao/Decimal(total)*taxas
    completo.append(parcial)
    rounded.append(round(parcial,2))
    sum += parcial
    print(parcial)

print(sum)

completo = np.array(completo)
rounded = np.array(rounded)

menos = completo - rounded

sum = np.sum(rounded)
while sum != taxas:
    value = np.max(np.abs(menos))
    idx = np.where(np.abs(menos) == value)
    rounded[idx] -= np.sign(rounded[idx])*Decimal(0.01)
