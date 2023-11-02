# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numbers = []
while True:
    numbers.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    while op not in ('S', 'N'):
        print('\033[31mErro!\033[m Digite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        op = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    if op == 'N':
        break
print('\033[34m=\033[m' * 60)
print('REPOSTAS'.center(60))
print('\033[34m=\033[m' * 60)
print(f'Foram digitados: \033[32m{len(numbers)} números\033[m.')
print(f'A lista ordenada de forma descrescente: \033[33m{sorted(numbers, reverse=True)}\033[m')
if 5 in numbers:
    print(f'O valor \033[32m5\033[m foi encontrado na lista \033[34m{numbers.count(5)} vez(es)\033[m.')
else:
    print(f'O valor \033[31m5, NÃO\033[m foi encontrado na lista.')
print('\033[34m=\033[m' * 60)
