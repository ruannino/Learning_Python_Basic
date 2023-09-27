# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os primeiros n elementos e
# uma sequência de Fibonacci.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)
print('=+' * 25)
print('SEQUÊNCIA DE FIBONACCI'.center(50))
print('=+' * 25)
n = int(input('Digite a quantidade de elementos em sequência: '))
n1 = 0
n2 = 1
print(f'\033[33m{n1}\033[m -> \033[33m{n2}\033[m ', end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(f'-> \033[33m{n3}\033[m ', end='')
    n1 = n2
    n2 = n3
    cont += 1
print('-> \033[31mFIM!\033[m')
print('=+' * 25)
