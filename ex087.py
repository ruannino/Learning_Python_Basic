# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
matriz = []
soma_pares = col_tres = m_linha = 0
for i in range(3):
    linha = []
    for n in range(3):
        valor = int(input(f'Digite o valor para a posição {(i, n)}'))
        linha.append(valor)
        if valor % 2 == 0:
            soma_pares += valor
        if n == 2:
            col_tres += valor
        if i == 1:
            m_linha += valor
    matriz.append(linha)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^3}]', end=' ')
    print()
print(f'A soma de todos os valores pares digitados {soma_pares}')
print(f'A soma dos valores da terceira coluna {col_tres}')
print(f'O maior valor da segunda linha {m_linha}')
