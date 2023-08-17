# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
somag = 0
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
for g in range(0, n):
    gols.append(int(input(f'Quantos gols o na partida {g + 1}: ')))
    somag += gols[g]
jogador['partidas'] = n
jogador['gols'] = gols
jogador['total'] = somag
print('=-' * 15)
print('{:^30}'.format('TABELA'))
print('=-' * 15)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
print()
for p, gp in enumerate(jogador['gols']):
    print(f'   => Na partida {p + 1}, fez {gp}')
print()
print(f'Foi um total de {jogador["total"]} gols. ')
print('=-' * 15)
