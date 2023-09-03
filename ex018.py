# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
# ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))
radiano = radians(angulo)
print(f'O ângulo de {angulo}º tem Seno: {sin(radiano):.2f}')
print(f'O ângulo de {angulo}º tem Cosseno: {cos(radiano):.2f}')
print(f'O ângulo de {angulo}º tem Tangente: {tan(radiano):.2f}')
