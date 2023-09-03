# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
from random import choice
aluno_1 = input('Digite o nome do 1º aluno: ')
aluno_2 = input('Digite o nome do 2º aluno: ')
aluno_3 = input('Digite o nome do 3º aluno: ')
aluno_4 = input('Digite o nome do 4º aluno: ')
sorteado = [aluno_1, aluno_2, aluno_3, aluno_4]
print(f'O aluno sorteado para apagar o quadro: {choice(sorteado)}')
