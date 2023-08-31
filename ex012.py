# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = str(input('Nome do Produto: '))
valor = float(input('Valor: R$'))
desconto = valor - (valor * (5 / 100))
print(f'O produto {produto} com desconto de 5% fica {desconto:.2f}')
