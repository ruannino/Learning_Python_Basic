# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as pessoas com idade acima da média.
ficha = {}
pessoas = []
soma = media = 0
while True:
    ficha.clear()
    ficha['nome'] = str(input('Digite o nome: ')).strip()
    while True:
        ficha['sexo'] = str(input('Digite o sexo: [M/F] ')).upper()[0].strip()
        if ficha['sexo'] in 'MF':
            break
        print('\033[31mERRO!\033[m digite M ou F...')
    ficha['idade'] = int(input('Digite a idade: '))
    soma += ficha['idade']
    pessoas.append(ficha.copy())

    while True:
        resp = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO!\033[m digite S ou N...')
    if resp == 'N':
        break
print('=-' * 12)
print("FICHA CADASTRO".center(40, '='))
print('=-' * 20)
print(f'O total de cadastros foi de {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'A média geral do grupo é de {media:5.2f} anos')
print('As mulheres cadastradas no grupo são ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'As pessoas com idade acima da média de {media:5.2f} são:')
for d in pessoas:
    if d['idade'] > media:
        print(f' => {d["nome"]} com {d["idade"]} anos.')
print("\033[31mENCERRANDO\033[m".center(40, '='))
