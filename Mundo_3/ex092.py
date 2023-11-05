# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se for o caso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. OBS: considerar 35 anos contribuição.
from datetime import date
ano_atual = date.today().year
ficha = dict()
ficha['Nome'] = str(input('Nome: ')).strip()
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
ficha['Idade'] = idade
CTPS = int(input('CTPS nº: '))
if CTPS != 0:
    ficha['CTPS'] = CTPS
    contrato = int(input('Ano de contratação: '))
    ficha['Contratação'] = (f'ano de {contrato}')
    ficha['Salário'] = float(input('Salário: R$ ').replace(',', '.'))
    aposentadoria = (idade + 35) - (ano_atual - contrato)
    ficha['Aposentadoria'] = (f'{aposentadoria} anos')
print('\033[33m=\033[m' * 40)
print(f'Ficha de {ficha["Nome"]}'.center(40))
print('\033[33m=\033[m' * 40)
for i, v in ficha.items():
    print(f'{i}  -->  {v}')
print('\033[33m=\033[m' * 40)
