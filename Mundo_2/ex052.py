# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('\033[32mE por isso ele é PRIMO!\033[m')
else:
    print('\033[31mE por isso ele NÃO é PRIMO\033[m')
