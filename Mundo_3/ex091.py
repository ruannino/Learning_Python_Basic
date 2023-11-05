# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# Dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('\033[34m=+\033[m' * 15)
print('JOGANDO DADOS'.center(30))
print('\033[34m=+\033[m' * 15)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('\033[34m=+\033[m' * 15)
print('\033[34m=+\033[m' * 15)
print('RANKING'.center(30))
print('\033[34m=+\033[m' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, n in enumerate(ranking):
    print(f'{i + 1}ª lugar > {n[0]} com {n[1]}.')
    sleep(1)
print('\033[34m=+\033[m' * 15)
