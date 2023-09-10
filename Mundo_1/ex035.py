# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = float(input('Coprimento da 1º linha: '))
r2 = float(input('Coprimento da 2º linha: '))
r3 = float(input('Coprimento da 3º linha: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'A soma das retas podem formar um \033[32mTRIÂNGULO!\033[m')
else:
    print(f'A soma das retas \033[31mNÃO\033[m podem formar um \033[31mTRIÂNGULO!\033[m')
