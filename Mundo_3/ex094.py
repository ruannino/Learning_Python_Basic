# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as pessoas com idade acima da média.
pessoa = dict()
galera = list()
cont_p = media_idade = somatoria = 0
while True:
    print('\033[32m-\033[m' * 30)
    print(f'Ficha da {cont_p + 1}ª pessoa'.center(30))
    print('\033[32m-\033[m' * 30)
    pessoa['Nome'] = str(input(f'Nome: ')).strip()
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['Idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    pessoa.clear()
    cont_p += 1
    print('\033[32m-\033[m' * 30)
    op = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    while op not in ('S', 'N'):
        print('\033[31mErro!\033[m Digite \033[33m"S"\033[m ou \033[33m"N"\033[m')
        op = str(input('Quer continuar ? \033[31m[S/N]\033[m: ')).strip().upper()
    if op == 'N':
        break
print('\033[32m-\033[m' * 50)
print(f'INFORMAÇÕES FINAIS'.center(50))
print('\033[32m-\033[m' * 50)
print(f'\nForam cadastradas {len(galera)} pessoas.')
for n in range(0, len(galera)):
    somatoria += galera[n]['Idade']
media_idade = somatoria / len(galera)
print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
print(f'\nAcima da média de idade do Grupo temos:')
for n in range(0, len(galera)):
    if media_idade < galera[n]['Idade']:
        print(f'\033[33m>> \033[m{galera[n]["Nome"]} com {galera[n]["Idade"]} anos.')
print('\033[32m-\033[m' * 50)
