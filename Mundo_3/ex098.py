# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
# a contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.  B) De 10 até 0, de 2 em 2.  C) Uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    print('\033[32m=' * 40)
    print(f'{"CONTADOR":^40}')
    print('=' * 40, end='')
    print('\033[m')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de \033[32m{i}\033[m até \033[32m{f}\033[m '
          f'de \033[32m{p}\033[m em \033[32m{p}\033[m!')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
print('\033[32m=\033[m' * 40)
print('Agora é sua vez...')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('\033[32m=\033[m' * 40)
