# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while. dec = (prim + (10 - 1) * raz)  # Fórmula do enésimo termo (PA).
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os primeiros termos da PA são: ')
while c < razao: range(termo, termo + 10 * razao, razao):
    print(f'\033[32m{c}\033[m', end=' \033[31m>\033[m ')
print('\033[32mFIM!\033[m')
