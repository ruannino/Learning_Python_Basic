# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
# a contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.  B) De 10 até 0, de 2 em 2.  C) Uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    for c in range(i, f + 1, p):
        print(f'{c} -> ', end='')
        sleep(1)
    print('FIM!')

contador(0, 10, 0)
contador(10, 0, 2)
