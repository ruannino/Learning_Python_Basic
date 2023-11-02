# Crie um programa onde o usuário possa digitar valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
numbers = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print(f'\033[32mNúmero \033[m{n}\033[32m adicionado com sucesso...\033[m')
    else:
        print(f'\033[33mNúmero \033[m{n}\033[33m já existe na lista. Não vou adicionar!\033[m')

    op = str(input('Deseja continuar ? \033[40m[S/N]\033[m: ')).strip().upper()
    while op not in ('S', 'N'):
        print('\033[31mErro! \033[mDigite \033[33m"S"\033[m ou \033[33m"N"\033[m...', end='')
        op = str(input('Deseja continuar ? \033[40m[S/N]\033[m: ')).strip().upper()

    if op == 'N':
        break
print('\033[32m=\033[m' * 60)
print('Lista Ordenada'.center(60))
print('\033[32m=\033[m' * 60)
print(f'A lista de números em ordem crescente: '
      f'\n>>> {sorted(numbers)}')
print('\033[32m=\033[m' * 60)
