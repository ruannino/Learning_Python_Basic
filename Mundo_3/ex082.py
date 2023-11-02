# Crie um programa que vai ler vários números e colocar em uma lista, Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
numbers = []
pares = []
impares = []
while True:
    numbers.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    while op not in ('S', 'N'):
        print('\033[31mErro!\033[m Digite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        op = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    if op == 'N':
        break
for n in numbers:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('\033[32m=\033[m' * 40)
print('RESULTADOS'.center(40))
print('\033[32m=\033[m' * 40)
print(f'lista Geral:   \033[40m{numbers}\033[m')
print(f'lista Pares:   \033[42m{pares}\033[m')
print(f'lista Ímpares: \033[43m{impares}\033[m')
print('\033[32m=\033[m' * 40)
