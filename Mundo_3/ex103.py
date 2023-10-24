# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(jogador='<desconhecido>', gols=0):
    print('-=' * 23)
    print(f'O Jogador {jogador} fez {gols} gols no campeonato!')
    print('=-' * 23)


jog = str(input('Nome do jogador: '))
gol = input('Nº de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
ficha(jog, gol)