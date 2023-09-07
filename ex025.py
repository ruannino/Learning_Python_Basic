# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite seu nome completo: '))
print(f'O nome digitado: {nome}')
print(f'O nome contém Silva ? {"SILVA" in nome.upper()}')
