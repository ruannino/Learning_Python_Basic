# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
time = []
jogador = {}
gols = []
while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols o {jogador["nome"]} fez na partida {g + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] :')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31mErro!\033[m digite S ou N...')
    if resp == 'N':
        break

print('=-' * 15)
print('{:^30}'.format('TIME'))
print('=-' * 15)
for e, j in enumerate(time):
    print(f'  => Jogador {e + 1}: {j["nome"]} - Total de gols {j["total"]}')
print('=-' * 15)

while True:
    cla = input('Deseja ver os dados de algum jogador ?\n'
                'Digite o índice do jogador ou [-1] para sair: ')
    if cla == "-1":
        break
    if cla.isdigit():
        cla = int(cla)
        if 1 <= cla <= len(time):
            jogador = time[cla - 1]
            print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}: ')
            for p, gp in enumerate(jogador['gols']):
                print(f'    => Na partida {p + 1}, fez {gp} gols(s).')
            print()
            print(f'Total de {jogador["total"]} de gol(s).')
            print('=-' * 15)
        else:
            print('Opção inválida! Digite um valor válido de jogador...')
    else:
        print('Opção inválida! Digite um valor válido de jogador...')
