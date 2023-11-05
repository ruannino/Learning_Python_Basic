# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for n in range(7):
    valor = int(input(f'Digite o \033[32m{n+1}º\033[m valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('\033[33m=\033[m' * 50)
print('RESULTADO'.center(50))
print('\033[33m=\033[m' * 50)
print(f'\nLista de pares > {numeros[0]}')
print(f'\nLista de ímpares > {numeros[1]}\n')
print('\033[33m=\033[m' * 50)
