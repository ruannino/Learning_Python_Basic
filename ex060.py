# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Método com biblioteca math
from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print(f'O fatorial de {num}! é {f}.')

# Método Extensivo
n = int(input('Digite um número: '))
c = n
m = c
while c > 0:
    if n == c:
        print(f'{n}! = {c} x ', end='')
        c -= 1
    else:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        m *= c
        c -= 1
print(f'{m}')

# Método com FOR
numb = int(input('Digite um número: '))
mul = numb
for c in range(numb, 0, -1):
    if numb == c:
        print(f'{numb}! = {c} x ', end ='')
    else:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        mul *= c
print(mul)
