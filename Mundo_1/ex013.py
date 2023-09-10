# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
funcionario = str(input('Nome do Funcionário: '))
salario_atual = float(input('Salário atual: '))
salario_aumento = salario_atual + (salario_atual * (15 / 100))
print(f'{funcionario} ganhou um aumento de 15%,\n'
      f'saiu de um salário de R${salario_atual},\n'
      f'agora passará a receber R${salario_aumento}.')
