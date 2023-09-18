# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos
mais_velho = soma = mais_nova = 0
homem_velho = ''
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}º pessoa: '))
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Digite o sexo de {nome}: \033[30m[M/F]\033[m')).strip().upper()
    soma += idade
    if 'F' in sexo[0] and idade < 20:
        mais_nova += 1
    elif idade > mais_velho and 'M' in sexo[0]:
        mais_velho = idade
        homem_velho = nome
media = soma / 4
print(f'As informações gerais do grupo:'
      f'\nA média de idade do grupo é de \033[32m{media:.2f}\033[m anos.'
      f'\nO homem mais venho se chama \033[32m{homem_velho}\033[m.'
      f'\nExistem \033[32m0{mais_nova}/033[m mulher(es) com menos de 20 anos.')
