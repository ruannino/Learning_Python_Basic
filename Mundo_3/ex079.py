# Crie um programa onde o usuário possa digitar valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
numbers = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Valor duplicado. Não foi adicionado...')
    r = str(input('Continue ? [S/N]: '))
    if r in 'Nn':
        break
numbers.sort()
print(f'Você digito os valores em em ordem crescente: {numbers}')
