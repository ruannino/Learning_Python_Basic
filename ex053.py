# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona
inverse = ''
frase = str(input('Digite uma frase qualquer: ')).upper().strip().split()
colar = ''.join(frase)
for c in range(0, len(colar), -1):
    inverse += colar[c]
print(colar, inverse)