# Crie um programa que vai ler vários números e colocar em uma lista, Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
numbers = []
pares = []
impares = []
while True:
    numbers.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    while op not in ('S', 'N'):
        print('Erro! Digite "S" ou "N"...', end='')
        op = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if op == 'N':
        break
for n in numbers:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'lista Geral: {numbers}')
print(f'lista Pares: {pares}')
print(f'lista Ímpares: {impares}')
