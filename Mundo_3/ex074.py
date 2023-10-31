# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
cont = maior = menor = 0
numeros_aleatorios = ((randint(0, 9)), (randint(0, 9)),
                      (randint(0, 9)), (randint(0, 9)),
                      (randint(0, 9)))
for n in numeros_aleatorios:
    if cont == 0:
        maior = n
        menor = n
        cont += 1
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('\033[33m=\033[m' * 50)
print('TUPLA ALEATÓRIA'.center(50))
print('\033[33m=\033[m' * 50)
print(f'Os valores sorteados foram: \033[32m{numeros_aleatorios}\033[m.')
print(f'O maior valor sorteado foi \033[31m{maior}\033[m.')
print(f'O menor valor sorteado foi \033[33m{menor}\033[m.')
print('\033[33m=\033[m' * 50)
