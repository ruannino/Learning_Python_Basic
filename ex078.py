# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numbers = []
minor = bigger = 0
for cont in range(0, 5):
    numbers.append(int(input(f'Digite o {cont + 1}º valor: ')))
    if cont == 0:
        minor = bigger = numbers[cont]
    else:
        if numbers[cont] < minor:
            minor = numbers[cont]
        if numbers[cont] > bigger:
            bigger = numbers[cont]
print(f'{"LISTAGEM":-^60}')
print(f'A lista completa: \033[40m{numbers}\033[m')
print(f'O menor número foi o \033[33m{minor}\033[m e está nas posições ', end='')
for i, v in enumerate(numbers):
    if v == minor:
        print(f'{i}...', end='')
print(f'\nO maior número foi o \033[33m{bigger}\033[m e está nas posições ', end='')
for i, v in enumerate(numbers):
    if v == bigger:
        print(f'{i}...', end='')
print()
print('-' * 60)
