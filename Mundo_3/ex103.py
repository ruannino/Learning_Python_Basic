# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato!'


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if n.strip() == '':
    if g.isnumeric():
        g = int(g)
        print(ficha(gols=g))
    else:
        print(ficha())
else:
    if g.isnumeric():
        g = int(g)
        print(ficha(n, g))
    else:
        print(ficha(nome=n))
