# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(lista):
    print('\033[34m=\033[m' * 40)
    print(f'SORTEANDO 05 NÚMEROS'.center(40))
    print('\033[34m=\033[m' * 40)
    print('Valores sorteados ', end='')
    c = 3
    while c != 0:
        sleep(0.5)
        print('\033[33m>\033[m', end=' ')
        c -= 1
    for cont in range(0, 5):
        sleep(0.5)
        valor = randint(1, 10)
        lista.append(valor)
        print(f'\033[32m{valor}\033[m ', end='')
    sleep(0.5)
    print('FIM!')
    sleep(0.5)
    print('\033[34m=\033[m' * 40)


def soma_par(lst):
    sleep(2)
    print('\033[35m=\033[m' * 40)
    print('SOMANDO PARES DE UMA LISTA'.center(40))
    print('\033[35m=\033[m' * 40)
    print('Analisando os números...')
    c = 3
    while c != 0:
        sleep(0.5)
        print('\033[31m> \033[m', end='')
        c -= 1
    soma = 0
    for n in lst:
        sleep(0.4)
        if n % 2 == 0:
            print(f'\033[32m{n}\033[m ', end='')
            soma += n
        else:
            print(f'\033[31m{n}\033[m ', end='')
    sleep(0.5)
    print(f'\n\033[40mRESULTADO ->', end='')
    sleep(0.5)
    print(f'{soma:>25}\033[m')
    print('\033[35m=\033[m' * 40)


numbers = list()
sorteia(numbers)
soma_par(numbers)
