# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os valores da lista...')
    print('=-' * 30)
    for num in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
        sleep(0.5)
        print(f'{n} ', end='')
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares {lista}, temos {soma}.')
    print('=-' * 30)


numeros = list()
sorteia(numeros)
somaPar(numeros)


