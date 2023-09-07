# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza
nome = str(input('Digite o nome completo: ')).split()
print('Muito prazer em te conhecer!')
primeiro_nome = nome[0]
ultimo_nome = nome[-1]
print(f'O seu primeiro nome é {primeiro_nome}.')
print(f'O seu último nome é {ultimo_nome}.')
