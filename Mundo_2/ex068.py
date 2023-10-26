# Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitória consecultivas que ele conquistou no final do jogo.

from random import randint
round = 0

while True:
    player = str(input('Par ou Ímpar ? ')).strip().upper()
    num_player = int(input('Digite um número de 0 a 10: '))
    num_cpu = randint(0, 10)
    if 'Í' in player or 'I' in player:
        choice_player = 'Ímpar'
        choice_cpu = 'Par'
    else:
        choice_player = 'Par'
        choice_cpu = 'Ímpar'
    sum = num_cpu + num_player
    if sum % 2 == 0:
        cong = 'Par'
    else:
        cong = 'Ímpar'
    if cong == choice_cpu:
        print(f'CPU = {num_cpu} + PLAYER = {num_player}. Total = {sum}, deu {cong}!')
        print('Você perdeu...', end='')
        break
    else:
        print(f'CPU = {num_cpu} + PLAYER = {num_player}. Total = {sum}, deu {cong}!')
        print('Você ganhou! Vamos novamente...')
        round += 1
print(f'Você durou {round} partidas.')
