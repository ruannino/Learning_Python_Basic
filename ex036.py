# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Valor do imóvel: R$'))
salario_comprador = float(input('Valor salarial: R$'))
numero_anos = int(input('Anos para pagamento: '))
porcentagem_salarial = (30 / 100) * salario_comprador
prestacoes_totais = numero_anos * 12
valor_por_prestacao = valor_casa / prestacoes_totais
if valor_por_prestacao <= porcentagem_salarial:
    print('Emprétimo Aprovado!')
#aprovacao_emprestimo
print(porcentagem_salarial)
