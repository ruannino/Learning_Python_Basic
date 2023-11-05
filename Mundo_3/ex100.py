# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores para lista: ', end='')
    for cont in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='')
    print('FIM!')


def soma_par(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares da lista {lst} é {soma}.')


numbers = list()
sorteia(numbers)
soma_par(numbers)
