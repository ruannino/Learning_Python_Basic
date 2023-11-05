# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = []
pares = []
impares = []
for n in range(7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print('\033[33m=\033[m' * 50)
print('RESULTADO'.center(50))
print('\033[33m=\033[m' * 50)
print(f'\nLista geral > {numeros}')
print(f'\nLista de pares > {pares}')
print(f'\nLista de ímpares > {impares}\n')
print('\033[33m=\033[m' * 50)
