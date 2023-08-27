# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.
from utilidadesCeV import moeda

v = float(input('Digite o valor do produto: R$ '))
p = int(input('Digite a porcentagem a incrementar: % '))
print(f'O valor do produto é {moeda.moeda(v)} com incremento de {p}% '
      f'tem o valor final de {moeda.aumentar(v, p, True)}')
print(f'O valor do produto é {moeda.moeda(v)} com desconto de {p}% tem o valor final de '
      f'{moeda.diminuir(v, p, True)}')
print(f'O dobro do valor é {moeda.dobro(v, True)}')
print(f'A metade do valor é {moeda.metade(v, True)}')
print(f'{moeda.moeda(v)}')
