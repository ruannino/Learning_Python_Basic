# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é \033[32mBISSEXTO\033[m!')
else:
    print(f'O ano {ano} \033[31mNÃO\033[m é \033[31mBISSEXTO\033[m!')
