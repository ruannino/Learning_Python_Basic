# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A)Qual é o total gasto na compra. B)Quantos produtos custam mais de R$1000. C)Qual é o nome do produto mais barato.
from time import sleep
prod_barato = ''
qnt_produtos = soma = prod_1000 = prec_prod_barato = 0
print('=' * 60)
print('Preçonildo Center Shopping'.center(60))
print('=' * 60)
while True:
    qnt_produtos += 1
    nome_produto = str(input(f'Nome do \033[33m{qnt_produtos}º\033[m Produto: '))
    preco_produto = float(input('Valor: \033[32mR$\033[m'))
    print('=' * 60)
    soma += preco_produto
    if qnt_produtos == 1:
        prod_barato = nome_produto
        prec_prod_barato = preco_produto
    elif qnt_produtos > 1 and preco_produto < prec_prod_barato:
        prod_barato = nome_produto
        prec_prod_barato = preco_produto
    if preco_produto >= 1000:
        prod_1000 += 1
    opcao = str(input('Continuar ? \033[40m[S/N]\033[m')).strip().upper()
    if 'N' in opcao:
        print('\033[31mEncerrando...\033[m')
        sleep(1)
        break
    if 'S' in opcao:
        print('\033[33mPróximo produto...\033[m')
        print('=' * 60)
        sleep(1)
print('=' * 60)
print(f'Total: \033[32mR${soma:.2f}\033[m.')
print('=' * 60)
sleep(1)
print(f'Item mais barato foi \033[33m{prod_barato}\033[m custando \033[32mR${prec_prod_barato:.2f}\033[m.')
print(f'Um total de \033[33m0{prod_1000} de produtos\033[m com valores acima de \033[32mR$1.000,00\033[m.')
print('=' * 60)
