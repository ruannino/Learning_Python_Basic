# Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitória consecultivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
round = 0

while True:
    print('\033[34m=\033[m' * 60)
    print('\033[33mJOGO PAR OU ÍMPAR\033[m'.center(60))
    print('\033[34m=\033[m' * 60)
    player = str(input('-------->   Par ou Ímpar ? ')).strip().upper()
    while True:
        num_player = int(input('Digite um número de 0 a 10: '))
        if 0 <= num_player <= 10:
            break
    num_cpu = randint(0, 10)
    if 'Í' in player or 'I' in player:
        choice_player = 'Ímpar'
        choice_cpu = 'Par'
    else:
        choice_player = 'Par'
        choice_cpu = 'Ímpar'
    sum = num_cpu + num_player
    if sum % 2 == 0:
        cong = 'Par'
    else:
        cong = 'Ímpar'
    print('\033[34mRESULTADO\033[m'.center(68,'-'))
    if cong == choice_cpu:
        print(f'CPU = {num_cpu} + PLAYER = {num_player}. Total = {sum}, deu {cong}!')
        sleep(1)
        print('\033[31m  >>> Você perdeu...', end='')
        break
    else:
        print(f'CPU = {num_cpu} + PLAYER = {num_player}. Total = {sum}, deu {cong}!')
        sleep(1)
        print('\033[32m  >>> Você ganhou! Vamos novamente...\033[m')
        round += 1
if round == 1:
    print(f'Você durou \033[m{round} \033[31mpartida.\033[m')
else:
    print(f'Você durou \033[m{round} \033[31mpartidas.\033[m')
print('=' * 60)
