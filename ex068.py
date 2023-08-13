# Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitória consecultivas que ele conquistou no final do jogo.

from random import randint
cont = 0

while True:
    print('\033[7m[ JOGO DE PAR OU ÍMPAR ]\033[m')
    print('=*' * 12)
    player = str(input('\033[40mVocê quer PAR ou ÍMPAR? \033[m')).strip().upper()
    num_player = int(input('Digite um número entre 0 e 10: '))
    cpu = randint(0, 10)

    if 'I' in player or 'Í' in player:
        choice_player = 'Ímpar'
        choice_cpu = 'Par'
    elif not 'I' in player or not 'Í' in player:
        choice_player = 'Par'
        choice_cpu = 'Ìmpar'

    rest = num_player + cpu
    result = rest

    if result % 2 == 0:
        comp = 'Par'
    elif result % 2 != 0:
        comp = 'Ímpar'

    if comp == choice_player:
        print(f'Deu \033[33m{rest}\033[m então é \033[32m{choice_player}\033[m.')
        print(f'\033[32mYOU WIN\033[m')
        print('\033[33m=*\033[m' * 12)
        cont += 1
    elif comp != choice_player:
        print(f'Deu \033[33m{rest}\033[m então é \033[32m{choice_cpu}\033[m.')
        print(f'Você teve \033[31m{cont}\033[m tentativas.')
        print(f'\033[31mYOU LOSE\033[m')
        break
