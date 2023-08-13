# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A)Qual é o total gasto na compra. B)Quantos produtos custam mais de R$1000. C)Qual é o nome do produto mais barato.
total = menor_preco = cont_k = 0
nome_menor = nome_produto = ''
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    nome_produto = str(input('\033[40mNome do produto: \033[m'))
    preco = float(input('\033[43mPreço: \033[32mR$\033[m'))
    choice = ' '
    while choice not in 'SN':
        choice = str(input('\033[42mQuer continuar?\033[7m [S/N] \033[m')).upper().strip()
    if total == 0 or preco < menor_preco:
        menor_preco = preco
        nome_menor = nome_produto
    total += preco
    if preco >= 1000:
        cont_k += 1
    if 'N' in choice:
        break
print('-' * 5, 'FIM DO PROGRAMA', '-' * 5)
print(f'O total da compra foi \033[32mR$ {total:.2f}.\033[m')
print(f'Temos \033[33m{cont_k} \033[mprodutos custando mais de \033[32mR$ 10000.00\033[m')
print(f'O produto mais barato foi \033[33m{nome_menor}\033[m que custa \033[32mR$ {menor_preco:.2f}.\033[m')
