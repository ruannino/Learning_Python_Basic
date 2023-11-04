# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
matriz = []
somapar = colunaT = mSL = ct = 0
for n in range(3):
    linha = []
    for i in range(3):
        valor = int(input(f'Digite o valor da posição [{n}, {i}]: '))
        linha.append(valor)
        if valor % 2 == 0:
            somapar += valor
        if i == 2:
            colunaT += valor
        if n == 1:
            if ct == 0:
                mSL = valor
                ct += 1
            elif ct == 1 and valor > mSL:
                mSL = valor
    matriz.append(linha[:])
print('\033[40m-\033[m' * 20)
print('MATRIZ'.center(20))
print('\033[40m-\033[m' * 20)
for n in range(3):
    for i in range(3):
        print(f'[{matriz[n][i]}]    ', end='')
    print()
print('\033[40m-\033[m' * 50)
print('RESULTADO'.center(50))
print('\033[40m-\033[m' * 50)
print(f'A soma de todos os valores pares é: {somapar}.')
print(f'A soma de todos os valores da terceira coluna é: {colunaT}.')
print(f'O maior valor da segunda linha é: {mSL}.')
print('\033[40m-\033[m' * 50)
