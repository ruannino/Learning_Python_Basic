# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
import time
todos_jogos = []
jogada = 0
jogos = int(input('Quantos jogos você quer gerar? '))

while len(todos_jogos) < jogos:
    jogada = []

    while len(jogada) < 6:
        sorteador = randint(1, 60)
        num = sorteador
        jogada.append(num)
    jogada.sort()

    if jogada not in todos_jogos:
        todos_jogos.append(jogada)

for jogada in todos_jogos:
    print(f'{jogada}')
    time.sleep(1)
