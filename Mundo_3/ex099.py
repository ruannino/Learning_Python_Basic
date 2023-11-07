# Faça um programa que tenha uma funcão chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.
def maior(* num):
    cont = top = 0
    for nu in num:
        if cont == 0:
            top = nu
            cont += 1
        elif cont >= 1:
            if nu > top:
                top = nu
            cont += 1
    print('\033[34m=\033[m' * 40)
    print('VERIFICADOR DE NÚMEROS'.center(40))
    print('\033[34m=\033[m' * 40)
    print(f'Recebi os números: ', end='')
    for n in num:
        print(f'\033[33m{n}\033[m ', end='')
    print(f',\nTotalizando: \033[33m{cont}\033[m números.')
    print(f'O maior foi o \033[33m{top}\033[m !')


maior(10, 8, 9, 13, 6)
maior(8, 2, 983, -4, 3)
maior(-3, -6, -9, -290)
