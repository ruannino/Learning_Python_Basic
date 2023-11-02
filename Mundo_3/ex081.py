# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numbers = []
while True:
    numbers.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    while op not in ('S', 'N'):
        print('Erro! Digite "S" ou "N"...', end='')
        op = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if op == 'N':
        break
print(f'Foram digitados: {len(numbers)} números.')
print(f'A lista ordenada de forma descrescente: {sorted(numbers, reverse=True)}')
if 5 in numbers:
    print(f'O valor 5 foi encontrado na lista {numbers.count(5)} vez(es).')
else:
    print(f'O valor 5 não foi encontrado na lista.')
