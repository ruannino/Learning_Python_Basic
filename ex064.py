# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag!)
cont = n = soma = 0
while n != 999:
    n = int(input('Digite um número \033[40m[999 to Exit]:\033[m '))
    if n != 999:
        cont += 1
        soma += n
print(f'A soma total dos \033[32m{cont}\033[m números digitado é \033[32m{soma}\033[m.')
