# Faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
soma = contador = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        contador += 1
        soma += i
print(f'A soma total dos \033[33m{contador}\033[m números ímpares divisíveis por 3;'
      f'\nNo intervalo de 1 à 500 é igual \033[32m{soma}\033[m.')
