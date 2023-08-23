# Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
# print(fatorial(5, show=True))   help(fatorial)


def fatorial(num, show=False):
    """
    -> Funçao calcula o fatorial de um número e exibe o resultado na tela.
    :param num: recebe o valor do número.
    :param show: parâmetro opcional para exibir ou não todo o calculo
    :return: retorna o fatorial de um número na tela.
    """
    f = 1
    for n in range(num, 0, -1):
        if show:
            print(f'{n}', end='')
            if n > 1:
                print(' * ', end='')
            else:
                print(' = ', end='')
        f *= n
    print(f'{f}')


fatorial(5, show=True)
