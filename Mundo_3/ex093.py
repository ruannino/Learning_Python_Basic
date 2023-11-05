# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
cont = somagol = contagem = 0
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input('Quantas partidas ele jogou: '))
gols = list()
while cont < partidas:
    gol = int(input(f'Quantos gols ele fez na {cont + 1}ª partida: '))
    cont += 1
    somagol += gol
    gols.append(gol)
mediagol = somagol / partidas
jogador['Partidas'] = partidas
jogador['Gols'] = gols
jogador['Total'] = somagol
if mediagol >= 1.3:
    jogador['Desepenho'] = '\033[33mFODÃO\033[m'
elif 0.5 < mediagol <= 1.2:
    jogador['Desepenho'] = '\033[32mPADRÃO\033[m'
elif mediagol < 0.5:
    jogador['Desepenho'] = '\033[31mMERRECA\033[m'
print('\033[32m=*\033[m' * 20)
print(f'Desempenho do jogador {jogador["Nome"]}'.center(40))
print('\033[32m=*\033[m' * 20)
print(f'Teve {jogador["Partidas"]} partidas jogadas')
for v in jogador['Gols']:
    if v > 1:
        print(f'Fez {v} gols na {contagem + 1}ª partida.')
    if v == 1:
        print(f'Fez {v} gol na {contagem + 1}ª partida.')
    elif v == 0:
        print(f'Fez nenhum gol na {contagem + 1}ª partida.')
    contagem += 1
print(f'Fez um total de {jogador["Total"]} gols.')
print(f'Seu desempenho é {jogador["Desepenho"]}')
print('\033[32m=*\033[m' * 20)
