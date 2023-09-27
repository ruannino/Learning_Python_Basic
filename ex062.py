# Melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar "0 termos"
from time import sleep
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = termo1
cont = 1
total = 0
mais_termos = 10
print('-' * 40)
print('Gerador de PA'.center(40))
print('-' * 40)
while mais_termos != 0:
    total += mais_termos
    while cont <= total:
        print(f'\033[32m{termo} \033[31m-> \033[m', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos mostrar a mais? '))
sleep(1)
print('\033[31mEncerrando...\033[m')
sleep(1)
print(f'Prograssão finalizada com \033[32m{total}\033[m termos exibidos.')
