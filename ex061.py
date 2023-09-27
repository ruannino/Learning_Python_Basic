# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = termo1
cont = 1
print('-' * 40)
print('Gerador de PA'.center(40))
print('-' * 40)
while cont <= 10:
    print(f'\033[32m{termo} \033[31m-> \033[m', end='')
    termo += razao
    cont += 1
print('\033[33mFIM!\033[m')
