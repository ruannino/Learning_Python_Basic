# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
boletim = dict()
boletim['aluno'] = str(input('Digite o nome: '))
boletim['media'] = float(input(f'Digite a média de {boletim["aluno"]}: '))
if boletim['media'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['media'] >= 5:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Reprovado'
print(F'{"BOLETIM":^20}')
print('=' * 20)
for k, v in boletim.items():
    print(f'{k:<10} : {v:<10}')