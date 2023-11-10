# Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.
from utilidadesCeV.moeda import aumentar, diminuir, dobro, metade

n = float(input('Digite o preço: R$'))
print(f'O sobro de R$ {n} é R$ {dobro(n)}')
print(f'A metade de R$ {n} é R$ {metade(n)}')
print(f'Aumento de {n} em 10% é R$ {aumentar(n, 10)}')
print(f'Diminuindo {n} em 20% é R$ {diminuir(n, 20)}')
