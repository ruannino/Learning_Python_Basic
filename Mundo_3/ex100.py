# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint


def sorteia(a):
    sor = list()
    for n in range(0, a):
        valor = randint(0, 100)
        sor.append(valor)
    print(f'Os números soteados foram {sor}.')
    return sor


def somaPar(lst):
    par = list()
    soma = 0
    for n in lst:
        if n % 2 == 0:
            par.append(n)
            soma += n
    print(f'A lista tem os seguintes números Pares {par} e a soma entre eles é {soma}.')


sorteia(5)
somaPar(sor)
