# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
# se o valor digitado for ímpar, desconsidere-o.
soma = 0
for n in range(1, 7):
    numero = int(input(f'Digite \033[33m{n}º\033[m número: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma total dos números pares digitados foi igual à \033[32m{soma}\033[m.')
