# Faça um programa que tenha uma funcão chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    print('=-' * 20)
    print('Analizando os valores passados...')
    big = 0
    c = 0
    for c, n in enumerate(num):
        print(f'{n} ', end='')
        if c == 0 or n > big:
            big = n
        sleep(1)
    print(f'Foram informados {c + 1} valores.')
    print(f'O maior valor informado foi {big} na porsição. {num.index(big)}')


maior(1, -2, 8, 4, 5)
maior(-3, -8, 0)
maior(-3, -5, -6)
maior(1, 0, 100)