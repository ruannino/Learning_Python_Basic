# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
dias = int(input('Dias de aluguel: '))
km = int(input('Km rodado: '))
aluguel_dias = dias * 60
aluguel_km = km * 0.15
total_aluguel = aluguel_km + aluguel_dias
print('-' * 40)
print(f'ALUGUEL DO VEICULO'.center(40))
print('-' * 40)
print(f'{dias} dias alugados: R${aluguel_dias:.2f}')
print(f'{km} KM rodados: R${aluguel_km:.2f}')
print('-' * 40)
print(f'Valor total: R${total_aluguel}')
