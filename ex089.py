# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# o boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
while True:
    nome = input('Nome Aluno: ')
    nota1 = float(input(f'Primeira nota de {nome}: '))
    nota2 = float(input(f'Segunda nota de {nome}: '))

    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])

    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if resposta[0] != 'S':
        break

print('{:^40}'.format('BOLETIM'))
print('-' * 40)
print('{:<5} {:<20} {:<8}'.format('Nº', 'NOME', 'MÉDIA'))
print('-' * 40)
for i, aluno in enumerate(alunos, start=1):
    print('{:<5} {:<20} {:<8}'.format(i, aluno[0], aluno[3]))
while True:
    mostrar_notas = int(input('mostrar notas de qual aluno ? [Digite o nº do aluno ou [0] para Sair: '))
    if mostrar_notas == 0:
        print('Encerrando...')
        break
    if 1 <= mostrar_notas <= len(alunos):
        aluno_escolhido = alunos[mostrar_notas - 1]
        print(f'Notas de {aluno_escolhido[0]} são {aluno_escolhido[1]} e {aluno_escolhido[2]}')
        print('-' * 45)
    else:
        print('Aluno não encontrado. Tente novamente...')
