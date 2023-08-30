# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# 1 = 4,89 cotação 30.08.2023
reais = float(input('Diga quantos reais você tem? R$'))
dolar = 4.89
qnt_dolares = reais / dolar
print(f'Você pode comprar {qnt_dolares:.2f}')
