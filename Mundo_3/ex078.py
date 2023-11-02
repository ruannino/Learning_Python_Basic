# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numbers = []
maior = menor = 0
for n in range(0, 5):
    numbers.append(int(input('Digite um valor: ')))
    if n == 0:
        maior = numbers[n]
        menor = numbers[n]
    else:
        if maior < numbers[n]:
            maior = numbers[n]
        if menor > numbers[n]:
            menor = numbers[n]
print('\033[34m=\033[m' * 50)
print('MAIOR E MENOR VALORES'.center(50))
print('\033[34m=\033[m' * 50)
print(f'A lista completa: \033[40m{numbers}\033[m')
print(f'O \033[32mmaior\033[m valor foi o \033[32m{maior}\033[m na posição ', end='')
for i, v in enumerate(numbers):
    if v == maior:
        print(f'\033[33m{i}\033[m...', end='')
print()
print(f'O \033[32mmenor\033[m valor foi o \033[32m{menor}\033[m na posição ', end='')
for i, v in enumerate(numbers):
    if v == menor:
        print(f'\033[33m{i}\033[m...', end='')
print()
print('\033[34m=\033[m' * 50)
