# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = []
for n in range(3):
    linha = []
    for i in range(3):
        valor = int(input(f'Digite o valor da posição [{n}, {i}]: '))
        linha.append(valor)
    matriz.append(linha[:])
print('\033[40m-\033[m' * 20)
print('MATRIZ'.center(20))
print('\033[40m-\033[m' * 20)
for n in range(3):
    for i in range(3):
        print(f'[{matriz[n][i]}]    ', end='')
    print()
print('\033[40m-\033[m' * 20)
