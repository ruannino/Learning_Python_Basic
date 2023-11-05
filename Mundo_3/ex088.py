# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. # 50.063.860
from random import randint
from time import sleep
all_games = []
game = []
loc = 1
n_games = int(input('Quantos jogos você deseja? '))
while True:
    cont = 0
    while cont < 6:
        n = randint(1, 60)
        if n not in game:
            game.append(n)
            cont += 1
    game.sort()
    if game not in all_games:
        all_games.append(game[:])
    game.clear()
    if len(all_games) == n_games:
        break
sleep(1)
print('\033[33m=\033[m' * 40)
print(f'{"MEGA SENA":<25}', f'JOGOS: {n_games}')
print('\033[33m=\033[m' * 40)
sleep(1)
for g in all_games:
    print(f'\nJogo \033[32m{loc}\033[m > ', end='')
    for v in g:
        print(f'{v} ', end='')
    loc += 1
    sleep(1)
print('\n')
print('\033[33m=\033[m' * 40)
print(f'\033[32m{"BOA SORTE!":^40}\033[m')
print('\033[33m=\033[m' * 40)
