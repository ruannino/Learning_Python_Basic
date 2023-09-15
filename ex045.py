# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
cpu = randint(1, 3)
cpu_choice = player_choice = 0
print('-' * 40)
print('JOKENPÔ'.center(40))
print('-' * 40)
player = int(input('''
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA
Qual a sua jogada ? '''))
if cpu == 1:
    cpu_choice = 'PEDRA'
elif cpu == 2:
    cpu_choice = 'PAPEL'
elif cpu == 3:
    cpu_choice = 'TESOURA'
if player == 1:
    player_choice = 'PEDRA'
elif player == 2:
    player_choice = 'PAPEL'
elif player == 3:
    player_choice = 'TESOURA'
sleep(1)
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ')
print('-' * 40)
if cpu == player:
    sleep(1)
    print(f'\033[30mCPU jogou,\033[m {cpu_choice}!')
    sleep(1)
    print(f'\033[30mPlayer jogou,\033[m {player_choice}!')
    print('-' * 40)
    sleep(1)
    print('\033[33mEMPATE!\033[m'.center(40))
elif cpu == 1 and player == 2 or cpu == 2 and player == 3 or cpu == 3 and player == 1:
    sleep(1)
    print(f'\033[30mCPU jogou,\033[m {cpu_choice}!')
    sleep(1)
    print(f'\033[30mPlayer jogou,\033[m {player_choice}!')
    print('-' * 40)
    sleep(1)
    print('\033[32mGANHOU!\033[m'.center(40))
elif cpu == 1 and player == 3 or cpu == 2 and player == 1 or cpu == 3 and player == 2:
    sleep(1)
    print(f'\033[30mCPU jogou,\033[m {cpu_choice}!')
    sleep(1)
    print(f'\033[30mPlayer jogou,\033[m {player_choice}!')
    print('-' * 40)
    sleep(1)
    print('\033[31mPERDEU!\033[m'.center(40))
