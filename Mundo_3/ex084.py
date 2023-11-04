# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves. MP = 100 ML = 70
galera = []
pessoa = []
cont = 1
MP = []
ML = []
while True:
    nome = str(input(f'Digite o nome da {cont}ª pessoa: '))
    peso = float(input('Digite o peso: '))
    resposta = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    pessoa.append(nome)
    pessoa.append(peso)
    galera.append(pessoa[:])
    pessoa.clear()
    while resposta not in ('S', 'N'):
        print('\033[31mErro!\033[m Digite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        resposta = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    if resposta == 'N':
        break
    cont += 1
for p in galera:
    if p[1] >= 100:
        MP.append(p[:])
    elif p[1] <= 70:
        ML.append(p[:])
print('\033[34m=\033[m' * 100)
print('RESULTADO DAS LISTAS DE CADASTRO'.center(100))
print('\033[34m=\033[m' * 100)
print(f'{"LISTA GERAL COM 0{} PESSOAS CADASTRADAS":-^100}'.format(cont))
for p in galera:
    print(f'-> Nome/Peso: {p[0]}, {p[1]:.2f}Kg')
print('\033[34m=\033[m' * 100)
print(f'{"LISTA DE PESSOAS ACIMA DOS 100KG":-^100}')
for p in MP:
    print(f'-> Nome/Peso: {p[0]}, {p[1]:.2f}Kg')
print('\033[34m=\033[m' * 100)
print(f'{"LISTA DE PESSOAS ACIMA DOS 100KG":-^100}')
for p in ML:
    print(f'-> Nome/Peso: {p[0]}, {p[1]:.2f}Kg')
print('\033[34m=\033[m' * 100)
