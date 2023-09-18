# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date
maior = menor = 0
atual = date.today().year
for i in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    if atual - nasc >= 18:
        maior += 1
    else:
        menor += 1
print(f'Existem \033[32m{menor} pessoas\033[m que ainda não atingiram a maioridade.'
      f'\nEnquanto \033[33m{maior} pessoas\033[m já são maiores de idade. ')