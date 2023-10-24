# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.

numbers = []
for cont in range(0, 5):
    n = float(input(f'Digite o {cont + 1}º : '))
    if cont == 0 or n >= numbers[-1]:
        numbers.append(n)
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                break
            pos += 1
print('-' * 30)
print(f'A lista ordenada fica: {numbers}.')
