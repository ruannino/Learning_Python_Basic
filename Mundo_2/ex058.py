# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cpu = randint(0, 10)
jogador = -1
cont = 0
print('-' * 60)
print('NÚMERO RANDOM'.center(60))
print('-' * 60)
print('\033[32mPensei em um número entre \033[33m0 e 10\033[32m, tente acertar...\033[m')
while cpu != jogador:
    cont += 1
    jogador = int(input(f'Sua \033[32m{cont}º\033[m tentativa: '))
    if jogador != cpu:
        if jogador > cpu:
            print(f'Você \033[31mERROU!\033[m o valor é menor, tente novamente...')
        elif jogador < cpu:
            print(f'Você \033[31mERROU!\033[m o valor é maior, tente novamente...')
print(f'\033[32mACERTOU!\033[m Levou \033[33m{cont}\033[m tentativas para conseguir!')
