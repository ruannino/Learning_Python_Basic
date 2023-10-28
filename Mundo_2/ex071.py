# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 40)
print('{:^40}'.format('BANCO MERCENÁRIO'))
print('=' * 40)
valor = int(input('Qual valor desejar sacar? R$'))
total = valor
cedula = 50
while True:
    if total >= cedula:
        num_cedulas = total // cedula
        total %= cedula
        if num_cedulas > 0:
            print(f'Total de \033[33m{num_cedulas} cédulas \033[mde \033[32mR${cedula}\033[m')

    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    if total == 0:
        break
print('=' * 40)