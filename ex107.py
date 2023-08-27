# Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.
from utilidadesCeV import moeda

v = float(input('Digite o valor do produto: R$ '))
p = int(input('Digite a porcentagem a incrementar: % '))
print(f'O valor do produto é {v} com incremento de {p}% tem o valor final de R${moeda.aumentar(v, p)}')
print(f'O valor do produto é {v} com desconto de {p}% tem o valor final de R${moeda.diminuir(v, p)}')
print(f'O dobro do valor é R${moeda.dobro(v)}')
print(f'A metade do valor é R${moeda.metade(v)}')
print(f'{moeda.moeda(v)}')
