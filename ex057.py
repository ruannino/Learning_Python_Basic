# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
repeat = 0
nome = str(input('Digite seu nome: '))
while repeat == 0:
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if 'M' in sexo[0] or 'F' in sexo[0]:
        if 'M' in sexo[0]:
            print(f'{nome} é do sexo MASCULINO!')
        elif 'F' in sexo[0]:
            print(f'{nome} é do sexo FEMININO!')
        repeat = 1
    else:
        print(f'\033[31mErro!\033[m Você digitou \033[33m> [{sexo}]...\033[mDigite um sexo válido!')
