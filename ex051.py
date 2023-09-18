# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
# No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os primeiros termos da PA são: ')
for c in range(termo, termo + 10 * razao, razao):
    print(f'\033[32m{c}\033[m', end=' \033[31m>\033[m ')
print('\033[32mFIM!\033[m')
