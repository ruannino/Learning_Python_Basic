# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número Real: '))
print(f'A porção inteira do valor é {math.trunc(num)}')  # Forma com a Biblioteca math
print(f'A porção inteira do valor é {num:.0f}')  # Forma com print
