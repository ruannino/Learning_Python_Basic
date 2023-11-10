# Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
# print(fatorial(5, show=True))   help(fatorial)
def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Número a ser calculado o fatorial.
    :param show: Paramêntro opcional de exibição ou não dos cálculos.
    :return: Retorna o resultado do fatorial de (n) número informado pelo usuário.
    Criado por Ruannino.
    """
    f = 1
    if show:
        print('\033[34m=\033[m' * 50)
        print(f'FATORIAL DE {n}! C/ CÁLCULOS'.center(50))
        print('\033[34m=\033[m' * 50)
        print(f'\033[33m{n}\033[31m!\033[m = ', end='')
    else:
        print('\033[34m=\033[m' * 50)
        print(f'FATORIAL DE {n}! S/ CÁLCULOS'.center(50))
        print('\033[34m=\033[m' * 50)
        print(f'\033[33m{n}\033[31m!\033[m = ', end='')
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'\033[34m{c}\033[m x ', end='')
            else:
                print(f'\033[34m{c}\033[m = ', end='')
        f *= c
    return f'\033[32m{f}\033[m'


# Programa Principal
print(fatorial(5, True))
