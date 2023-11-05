# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).strip()
aluno['Média'] = float(input('Média do aluno: ').replace(',', '.'))
if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[32mAprovado\033[m'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'em \033[33mRecuperação\033[m'
elif aluno['Média'] < 5:
    aluno['Situação'] = '\033[31mReprovado\033[m'
print('\033[35m=\033[m' * 30)
print(f'{aluno["Nome"]:^30}')
print('\033[35m=\033[m' * 30)
print(f'\nMédia --> {aluno["Média"]:.1f}')
print(f'\nO aluno está {aluno["Situação"]}.')
print('\033[35m=\033[m' * 30)
