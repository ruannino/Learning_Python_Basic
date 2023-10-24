# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se for o caso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. OBS: considerar 35 anos contribuição.
from datetime import date
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - ano_de_nascimento
ficha['idade'] = idade
n_trabalho = int(input('Carteirta de Trabalho (0 não tem): '))
if n_trabalho != 0:
    ficha['CTPS'] = n_trabalho
    ano_contratacao = int(input('Ano de Contratação: '))
    contract = date.today().year - ano_contratacao
    ficha['Ano de Contratação'] = ano_contratacao
    ficha['Salário'] = float(input('Salário: R$ '))
    aposentadoria = (35 - contract) + idade
    ficha['Aposentadoria'] = aposentadoria
print('=-' * 15)
print('{:^=30}'.format("FICHA"))
print('=-' * 15)
for k, v in ficha.items():
    print(f'- {k} tem o valor {v}')
