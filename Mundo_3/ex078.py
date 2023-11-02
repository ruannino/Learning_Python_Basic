# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numbers = []
maior = menor = 0
for n in range(0, 5):
    numbers.append(int(input('Digite um valor: ')))
    if n == 0:
        maior = numbers[n]
        menor = numbers[n]
    else:
        if maior < numbers[n]:
            maior = numbers[n]
        if menor > numbers[n]:
            menor = numbers[n]
print(f'A lista completa: {numbers}')
print(f'O maior valor foi o {maior} na posição {numbers.index(maior)}')
print(f'O maior valor foi o {menor} na posição {numbers.index(menor)}')
