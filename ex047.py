# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
for p in range(0, 51, 1):
    if p % 2 == 0:
        print(f'\033[32m{p} \033[33m->\033[m ', end='')
print('\033[31mFIM!\033[m')
