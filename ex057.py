# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
nome = str(input('Digite seu nome: '))
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
while sexo[0] not in 'MF':
    sexo = str(input(f'\033[31mErro!\033[m Digite um sexo válido: ')).strip().upper()
print(f'\033[33m{nome}\033[m é do sexo \033[33m{sexo}\033[m, registrado com sucesso.')
