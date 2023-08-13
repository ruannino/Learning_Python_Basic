# Crie um progra que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('{:^30}'.format('BANCO MERCENÁRIO'))
print('=' * 30)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
cedula = 50
total_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1
    else:
        if total_ced != 0:
            print(f'Total de \033[33m{total_ced} cédulas\033[m de \033[32mR${cedula}\033[m')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 30)
print('{:^30}'.format('VOLTE SEMPRE!'))
