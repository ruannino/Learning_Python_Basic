# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
aluno = str(input('Nome do aluno: ')).upper()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('-' * 40)
print(f'3BOLETIM DO {aluno}'.center(40))
print('-' * 40)
print(f'Nota #1:     \033[32m{nota1:.1f}\033[m')
print(f'Nota #2:     \033[32m{nota2:.1f}\033[m')
print('-' * 40)
print(f'Média:       \033[33m{media:.1f}\033[m')
