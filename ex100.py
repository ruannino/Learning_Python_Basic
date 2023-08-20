# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint
def sorteia():
    numeros = list()
    for num in range(0, 5):
        n = randint(0, 100)
        numeros.append(n)
    print(numeros)


def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 ==0:
            soma += num


sorteia()
