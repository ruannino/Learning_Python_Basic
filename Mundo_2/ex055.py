# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
menor = maior = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da \033[32m{c}º\033[m pessoa: kg'))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O \033[31mmaior\033[m peso foi de \033[31m{maior:.2f}\033[mKg.'
      f'\nO \033[33mmenor\033[m peso foi de \033[33m{menor:.2f}\033[mKg.')
