# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número Real: '))
print(f'A porção inteira do valor é {trunc(num)}')  # Forma com a Biblioteca math
print(f'A porção inteira do valor é {int(num)}')  # Forma com print int
