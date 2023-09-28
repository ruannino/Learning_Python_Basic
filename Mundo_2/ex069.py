# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa devrá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

cont_G = cont_M = cont_H = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    choice = ' '
    while choice not in 'SN':
        choice = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if 'F' in sexo:
        if idade <= 20:
            cont_M += 1
    elif 'M' in sexo:
        cont_H += 1
    if idade >= 18:
        cont_G += 1
    if 'N' in choice:
        break
print(f'Total de pessoas com mais de 18 anos: {cont_G}')
print(f'Total de Homens cadastrados: {cont_H}')
print(f'O total de mulheres que tem menos de 20 anos: {cont_M}')
