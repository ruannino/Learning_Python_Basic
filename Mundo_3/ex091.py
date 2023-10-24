# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# Dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Jogando Dados...')
print('-' * 30)
sleep(1)

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('{:-^30}'.format('RESULTADO'))
sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i + 1}º lugar foi o {v[0]} com {v[1]}')
    sleep(1)
print('=' * 30)
