# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
numbers = []
for n in range(0, 5):
    v = int(input('Digite um valor: '))
    if n == 0 or v >= numbers[-1]:
        numbers.append(v)
        print('Número adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numbers):
            if v <= numbers[pos]:
                numbers.insert(pos, v)
                print(f'O número foi adicionado a posição \033[33m{pos}\033[m da lista.')
                break
            pos += 1
print('\033[35m=\033[m' * 40)
print('NÚMEROS EM ORDEM CRESCENTE'.center(40))
print('\033[35m=\033[m' * 40)
print(f'{numbers}'.center(40))
print('\033[35m-\033[m' * 40)
