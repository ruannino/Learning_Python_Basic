# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cpu = randint(0, 10)
jogador = -1
cont = 0
print('-' * 40)
print('NÚMERO RANDOM'.center(40))
print('-' * 40)
print('Pensei em um número, tente acertar...')
while cpu != jogador:
    cont += 1
    jogador = int(input(f'Sua {cont}º tentativa: '))
    if jogador != cpu:
        print(f'Você \033[31mERROU!\033[m tente novamente...')
print(f'\033[32mVENCEU!\033[m Levou \033[33m{cont}\033[m tentativas para conseguir!')
