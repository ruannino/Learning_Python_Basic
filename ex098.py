# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
# a contragem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.  B) De 10 até 0, de 2 em 2.  C) Uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    cont = i
    sleep(1)
    print(f'Contando de {i} até {f} de {p} em {p}:')
    if i < f:
        while cont <= f:
            print(f' {cont}', end='')
            cont += p
            sleep(0.5)
        print()
    elif i > f:
        while cont >= f:
            print(f' {cont}', end='')
            cont -= p
            sleep(0.5)
        print()


def lin():
    print('~' * 40)


contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é a sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
lin()
