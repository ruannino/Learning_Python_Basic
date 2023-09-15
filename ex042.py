# Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero: todos os lados iguais;
# - isósceles: dois lados iguais;
# - escaleno: todos os lados diferentes;
r1 = float(input('Coprimento da 1º linha: '))
r2 = float(input('Coprimento da 2º linha: '))
r3 = float(input('Coprimento da 3º linha: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'A soma das retas podem formar um \033[32mTRIÂNGULO!\033[m')
    if r1 == r2 == r3:
        print('O triângulo formado é um \033[32mEQUILÁTERO\033[m,'
              '\nonde todos os lados são iguais.')
    elif r1 == r2  or r1 == r3 or r2 == r3:
        print('O triângulo formado é um \033[34mISÓSCELES\033[m,'
              '\nonde dois lados são iguais.')
    else:
        print('O triângulo formado é um \033[33mESCALENO\033[m,'
              '\nonde todos os lados são diferentes.')
else:
    print(f'A soma das retas \033[31mNÃO\033[m podem formar um \033[31mTRIÂNGULO!\033[m')
