# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# o boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
all_class = []
aluno = []
indice = 0
print('\033[34m=\033[m' * 50)
print('CADASTRO DE NOTAS'.center(50))
print('\033[34m=\033[m' * 50)
while True:
    nome = str(input('Nome do Aluno(a): ')).strip()
    aluno.append(nome)
    while True:
        nota1 = float(input('Nota #1: ').replace(',', '.'))
        if 0 <= nota1 <= 10:
            break
        else:
            print('\033[31mErro!\033[m Digite uma nota válida entre \033[33m0\033[m e \033[33m10\033[m...')
    aluno.append(nota1)
    while True:
        nota2 = float(input('Nota #2: ').replace(',', '.'))
        if 0 <= nota2 <= 10:
            break
        else:
            print('\033[31mErro!\033[m Digite uma nota válida entre \033[33m0\033[m e \033[33m10\033[m...')
    aluno.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)
    all_class.append(aluno[:])
    aluno.clear()
    print('\033[34m-\033[m' * 50)
    resp = str(input('Quer continuar? \033[40m[S/N]\033[m: ')).strip().upper()
    while resp not in ('S', 'N'):
        print('\033[31mErro! \033[mDigite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        resp = str(input('Quer continuar? \033[40m[S/N]\033[m: ')).strip().upper()
    if resp == 'N':
        break
print('\033[34m=\033[m' * 50)
print('BOLETIM DA CLASSE'.center(50))
print('\033[34m=\033[m' * 50)
for a in all_class:
    print(f'\033[33m#{indice} \033[34mAluno: \033[m{a[0]:<18}', end='')
    if a[3] >= 7:
        print(f'\033[34mMédia: \033[32m{a[3]:.1f}\033[m')
    elif 5 <= a[3] < 7:
        print(f'\033[34mMédia: \033[33m{a[3]:.1f}\033[m')
    elif a[3] < 5:
        print(f'\033[34mMédia: \033[31m{a[3]:.1f}\033[m')
    print()
    indice += 1
print('\033[34m=\033[m' * 50)
while True:
    notas = int(input(f'De qual aluno você gostaria de ver as notas ?\n'
                      f'Índice do Aluno de \033[40m[0 à {indice}]\033[m|[EXT:\033[33m-1\033[m]: '))
    while notas > indice:
        print('\033[31mErro!\033[m Digite um valor de Índice válido...')
        notas = int(input(f'Índice do Aluno de \033[40m[0 à {indice}]\033[m|[EXT:\033[33m-1\033[m]: '))
    if notas < 0:
        sleep(1)
        print('\033[31m> ', end='')
        sleep(1)
        print('> ', end='')
        sleep(1)
        print('> ', end='')
        sleep(1)
        print('  Encerrando...\033[m')
        sleep(1)
        print('\033[34m=\033[m' * 50)
        break
    else:
        print('\033[34m=\033[m' * 50)
        print(f'NOTAS DO ALUNO'.center(40))
        print('\033[34m=\033[m' * 50)
        print(f'\033[34mAluno(a):\033[m {all_class[notas][0]}')
        if all_class[notas][1] >= 7:
            print(f'\033[34mNota 1\033[m --->  \033[32m{all_class[notas][1]:.1f}\033[m')
        elif 5 <= all_class[notas][1] < 7:
            print(f'\033[34mNota 1\033[m --->  \033[33m{all_class[notas][1]:.1f}\033[m')
        elif all_class[notas][1] < 5:
            print(f'\033[34mNota 1\033[m --->  \033[31m{all_class[notas][1]:.1f}\033[m')

        if all_class[notas][2] >= 7:
            print(f'\033[34mNota 1\033[m --->  \033[32m{all_class[notas][2]:.1f}\033[m')
        elif 5 <= all_class[notas][2] < 7:
            print(f'\033[34mNota 1\033[m --->  \033[33m{all_class[notas][2]:.1f}\033[m')
        elif all_class[notas][2] < 5:
            print(f'\033[34mNota 1\033[m --->  \033[31m{all_class[notas][2]:.1f}\033[m')
        print('\033[34m=\033[m' * 50)
print(f'{"FIM":x^50}')
