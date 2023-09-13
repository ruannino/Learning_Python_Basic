# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
print('-' * 80)
print('SIMULADOR DE EMPRÉSTIMO'.center(80))
print('-' * 80)
valor_casa = float(input('Valor do imóvel: R$'))
salario_comprador = float(input('Valor salarial: R$'))
numero_anos = int(input('Anos para pagamento: '))
porcentagem_salarial = (30 / 100) * salario_comprador
prestacoes_totais = numero_anos * 12
valor_por_prestacao = valor_casa / prestacoes_totais
if valor_por_prestacao <= porcentagem_salarial:
    print('-' * 80)
    print('\033[32mEmprétimo APROVADO!\033[m')
    print(f'O valor do empréstimo total \033[32mR${valor_casa:.2f}\033[m.')
    print(f'O pagamento: \033[33m{prestacoes_totais}\033[m X \033[32mR${valor_por_prestacao:.2f}\033[m.')

elif valor_por_prestacao > porcentagem_salarial:
    print('-' * 80)
    print('\033[31mEmpréstimo NEGADO!\033[m')
    print('A parcela do empréstimo excedeu \033[31m30%\033[m do seu salário.')
print('-' * 40)
