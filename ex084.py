# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves. MP = 100 ML = 70
pessoas = []
MP = []
ML = []
while True:
    nome = str(input('Nome da pessoa: ')).strip()
    peso = float(input('Qual a peso: '))
    pessoas.append((pessoas, peso))

    if peso >= 100:
        MP.append(nome)
    elif peso <= 70:
        ML.append(nome)

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resposta in 'N':
        break

print(f'O número de pessoas cadastradas é {len(pessoas)}')
print(f'As pessoas mais pesadas são: {MP}')
print(f'As pessoas mais leves são: {ML}')
