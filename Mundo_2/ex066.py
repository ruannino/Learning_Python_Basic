# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
# que é a condição de parada (flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
soma = c = 0
while True:
    n = int(input('\033[31mDigite um número: \033[m'))
    if n == 999:
        break
    soma += n
    c += 1
print('=-' * 20)
print(f'O valor da soma dos \033[33m{c}\033[m valores é \033[32m{soma}\033[m.')
print('=-' * 20)
