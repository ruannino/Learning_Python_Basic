# Faça um programa que mostre na tela uma contagem regressiva para o estouro e fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Cotagem regressiva para queima de Fogos!')
sleep(1)
for c in range (10, -1, -1):
    if c >= 7:
        print(f'\033[32m{c}\033[m')
        sleep(1)
    elif c >= 4:
        print(f'\033[33m{c}\033[m')
        sleep(1)
    elif c <= 3:
        print(f'\033[31m{c}\033[m')
        sleep(1)
print('\033[31mBUM!\033[m', end='')
sleep(0.5)
print('\033[33mPOOOW!\033[m', end='')
sleep(0.5)
print('\033[35mPAAAW!\033[m')
sleep(0.3)
print('\033[31mPARÁ!\033[m', end='')
sleep(0.3)
print('\033[33mPÁÁÁ!\033[m', end='')
sleep(0.3)
print('\033[35mPOOOW!\033[m')
