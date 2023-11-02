# Crie um programa onde o usuário possa digitar valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
numbers = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print(f'Número {n} adicionado com sucesso...')
    else:
        print(f'Número {n} já existe na lista. Não vou adicionar!')

    op = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    while op not in ('S', 'N'):
        print('Erro! Digite "S" ou "N"...', end='')
        op = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    if op == 'N':
        break

print(f'A lista de números em ordem crescente: {sorted(numbers)}')
