# Faça um programa que mostre na tela uma contagem regressiva para o estouro e fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Cotagem regressiva para queima de Fogos!')
sleep(1)
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('\033[31mBUM!\033[m', end='')
sleep(0.5)
print('\033[33mPOW!\033[m', end='')
sleep(0.5)
print('\033[35mPAH!\033[m')
