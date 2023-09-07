# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cidade = str(input('Digite o nome da cidade: '))
fatiado = cidade.split()
comp = "SANTO" in fatiado[0].upper()
print(f'A cidade começa com Santo ? {comp}')
