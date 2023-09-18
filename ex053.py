# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona
frase = str(input('Digite uma frase qualquer: ')).upper().strip().replace(" ", "")
inverse = frase[::-1]
if frase == inverse:
    print(f'\033[32mA frase é um PALÍNDROMO!\033[m')
else:
    print(f'\033[31mNÃO é um palíndromo!\033[m')
