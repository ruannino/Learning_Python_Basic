# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogadores = list()
jogador = dict()
while True:
    cont = somagol = 0
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
    jogadores.append(jogador.copy())
    jogador.clear()
    opcao = str(input('Deseja continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    while opcao not in ('S', 'N'):
        print('\033[31mErro!\033[m Digite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        opcao = str(input('Deseja continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    if opcao == 'N':
        break
n = 0
print('\033[32m=*\033[m' * 30)
print(f'Desempenho dos Jogadores no Campeonato'.center(60))
print('\033[32m=*\033[m' * 30)
print(f'{"nº":<7}{"Nome":^38}{"Total gols":>15}')
print('\033[32m-\033[m' * 60)
for i in jogadores:
    print(f'{n:<7}{jogadores[n]["Nome"]:^38}{jogadores[n]["Total"]:>15}')
    n += 1
print('\033[32m=*\033[m' * 30)
while True:
    contagem = 0
    op = int(input(f'Digite o indice do Jogador para detalhes ou [-1] para sair: '))
    if 0 <= op < len(jogadores):
        print('\033[32m=*\033[m' * 30)
        print(f'Desempenho do jogador {jogadores[op]["Nome"]}'.center(60))
        print('\033[32m=*\033[m' * 30)
        print(f'Teve {jogadores[op]["Partidas"]} partidas jogadas')
        for v in jogadores[op]['Gols']:
            if v > 1:
                print(f'Fez {v} gols na {contagem + 1}ª partida.')
            if v == 1:
                print(f'Fez {v} gol na {contagem + 1}ª partida.')
            elif v == 0:
                print(f'Fez nenhum gol na {contagem + 1}ª partida.')
            contagem += 1
        print(f'Fez um total de {jogadores[op]["Total"]} gols.')
        print(f'Seu desempenho é {jogadores[op]["Desepenho"]}')
        print('\033[32m=*\033[m' * 30)
    if op == -1:
        print('\033[31m>>>>> Encerrando...\033[m')
        break
    else:
        print(f'\033[31mErro!\033[m Digite um índice válido entre '
              f'\033[33m0\033[m e \033[33m{len(jogadores) - 1}\033[m...')
