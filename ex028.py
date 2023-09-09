# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = randint(0, 5)
print(f'{"Olá, eu sou o Randomitron!":^40}')
print('-' * 40)
print('Pensei em um número entre 0 e 5...')
usuario = int(input('...tente advinhar o número, qual seu palpite? '))
if usuario == n:
    print('\033[33mPROCESSANDO...\033[m')
    sleep(1)
    print(f'Você ganhou o número foi o {n} mesmo!')
else:
    print('\033[33mPROCESSANDO...\033[m')
    sleep(1)
    print(f'Você perdeu o número foi o {n}, tente novamente!')
