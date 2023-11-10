# Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.
from utilidadesCeV.moeda import aumentar, diminuir, dobro, metade

print(aumentar(500, 10))
print(diminuir(500, 10))
print(dobro(500))
print(metade(500))
