# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numbers = ((randint(0,10)), (randint(0,10)), (randint(0,10)),
           (randint(0,10)),(randint(0,10)))
print(f'O números sorteados: {numbers}')
print(f'O maior número foi o {max(numbers)}')
print(f'O menor número foi o {min(numbers)}')
