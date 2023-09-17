# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal, e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até 2x no cartão: preço normal;
# - em 3x ou mais no cartão: 20% de juros;
valor_produto = float(input('Valor do produto: R$'))
print('-' * 80)
print('PRODUTO'.center(80))
print('-' * 80)
forma_pagamento = int(input('''
\033[40m[ 1 ]\033[m - À vista dinheiro/cheque;
\033[40m[ 2 ]\033[m - À vista no cartão;
\033[40m[ 3 ]\033[m - Em até 2x no cartão;
\033[40m[ 4 ]\033[m - Em 3x ou mais no cartão;
Qual a forma de pagamento? 
'''))
print('-' * 80)
if forma_pagamento == 1:
    dinheiro_cheque = valor_produto - (10 / 100) * valor_produto
    print(f'Você terá 10% de desconto. O valor a ser pago é \033[32mR${dinheiro_cheque:.2f}\033[m')
elif forma_pagamento == 2:
    av_cartao = valor_produto - (5 / 100) * valor_produto
    print(f'Você terá \033[34m5% de desconto\033[m. O valor a ser pago é \033[32mR${av_cartao:.2f}\033[m')
elif forma_pagamento == 3:
    print(f'O valor a ser pago é \033[32mR${valor_produto:.2f}\033[m')
elif forma_pagamento == 4:
    av_cartao = valor_produto + (20 / 100) * valor_produto
    print(f'Você terá \033[34m20% de acréscimo\033[m. O valor a ser pago é \033[32mR${av_cartao:.2f}\033[m')
else:
    print('\033[31mERRO! Você digitou uma forma de pagamento inválida.\033[m')
print('-' * 80)
