# Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores
# como um valor monetário formatado.
from utilidadesCeV import moeda

v = float(input('Digite o valor do produto: R$ '))
p = int(input('Digite a porcentagem a incrementar: % '))
print(f'O valor do produto é {moeda.moeda(v)} com incremento de {p}% tem o valor final de '
      f'{moeda.moeda(moeda.aumentar(v, p))}')
print(f'O valor do produto é {moeda.moeda(v)} com desconto de {p}% tem o valor final de '
      f'{moeda.moeda(moeda.diminuir(v, p))}')
print(f'O dobro do valor é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade do valor é {moeda.moeda(moeda.metade(v))}')
print(f'{moeda.moeda(v)}')
