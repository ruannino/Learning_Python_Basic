# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[], []]
for n in range(0, 7):
    valor = int(input('Digite um valor: '))

    if valor % 2 == 0:
        numbers[0].append(valor)
    else:
        numbers[1].append(valor)

numbers[0].sort()
numbers[1].sort()

print(f'Os válores pares em ordem crescente é {numbers[0]}')
print(f'Os válores ímpares em ordem crescente é {numbers[1]}')
