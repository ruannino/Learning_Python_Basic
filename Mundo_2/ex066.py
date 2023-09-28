# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
# que é a condição de parada (flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
soma = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'O valor da soma dos {c} valores é {soma}')
