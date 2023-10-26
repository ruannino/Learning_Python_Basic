# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
cont = 1
maiorDezoito = mulheresVinte = homens = 0
opcao = ''
while True:
    print('=' * 40)
    print(f'*== Ficha #{cont} ==*'.center(40))
    print('=' * 40)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    if idade > 18:
        maiorDezoito += 1
    sexo = str(input('Sexo[F/M]: ')).strip().upper()
    cont += 1
    if idade < 20 and 'F' in sexo:
        mulheresVinte += 1
    if 'M' in sexo:
        homens += 1
    opcao = str(input('Quer continuas [N/S]: ')).strip().upper()
    if 'N' in opcao:
        break
print(f'Foram cadastradas {maiorDezoito} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homens} homem(ns).')
print(f'Foram cadastradas {mulheresVinte} mulher(es) menores de 20 anos.')
