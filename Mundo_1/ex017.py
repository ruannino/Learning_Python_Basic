# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)  # Método com cálculos
hipotenusa2 = hypot(cateto_oposto, cateto_adjacente)  # Método com biblioteca math
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
print(f'A hipotenusa com o math vai medir {hipotenusa2:.2f}')
