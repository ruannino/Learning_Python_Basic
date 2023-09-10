# Crie um programa que leia o nome completo de uma pessoa:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome:
nome = str(input('Digite o nome: ')).strip()
print(f'Você digitou: {nome}')
print('Agora o que foi pedido...')
print('-' * 40)
print(f'O nome em maiúsculo: {nome.upper()}')
print(f'O nome em minúsculo: {nome.lower()}')
fatiar = nome.split()
print(f'O número de letras total s/ espaços: {len(fatiar[0])}')
reagrupar = ''.join(fatiar)
print(f'O número de letras total do 1º nome: {len(reagrupar)}')
print('-' * 40)
