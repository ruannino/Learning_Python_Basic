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
    nome_produto = str(input(f'Nome do {qnt_produtos}º Produto: '))
    preco_produto = float(input('Valor: R$'))
    print('=' * 60)
    soma += preco_produto
    if qnt_produtos == 1:
        prod_barato = nome_produto
        prec_prod_barato = preco_produto
    elif qnt_produtos > 1 and preco_produto < prec_prod_barato:
        prod_barato = nome_produto
        prec_prod_barato = preco_produto
    if preco_produto > 1000:
        prod_1000 += 1
    opcao = str(input('Continuar ? [S/N]')).strip().upper()
    if 'N' in opcao:
        print('Encerrando...')
        sleep(1)
        break
    if 'S' in opcao:
        print('próximo produto...')
        print('=' * 60)
        sleep(1)
print('=' * 60)
print(f'Total: \033[32mR${soma:.2f}\033[m.')
print('=' * 60)
sleep(10)
print(f'Item mais barato foi {prod_barato} custando R${prec_prod_barato:.2f}.')
print(f'Um total de 0{prod_1000} de produtos com valores acima de R$1.000,00.')
print('=' * 60)
