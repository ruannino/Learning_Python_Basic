def aumentar(v=0, p=0, format=False):
    """
    -> Aumenta o valor, segundo a porcentagem definida.
    :param v: Valor para incremento.
    :param p: Porcentagem de incremento.
    :param format: Retorna ou não o valor convertido em moeda.
    :return: Retorna o valor aumentado segundo a porcetagem escolhida.
    Criado por Ruannino.
    """
    res = v + (p / 100) * v
    return res if format is False else sifra(res)


def diminuir(v=0, p=0, format=False):
    """
    -> Diminui o valor, segundo a porcentagem definida.
    :param v: Valor para redução.
    :param p: Porcentagem de redução.
    :param format: Retorna ou não o valor convertido em moeda.
    :return: Retorna o valor diminuido segundo a porcetagem escolhida.
    Criado por Ruannino.
    """
    res = v - (p / 100) * v
    return res if format is False else sifra(res)


def dobro(v=0, format=False):
    """
    -> Dobra o valor de entrada.
    :param v: Valor para dobrar.
    :param format: Retorna ou não o valor convertido em moeda.
    :return: Retorna o valor dobrado.
    Criado por Ruannino.
    """
    res = v * 2
    return res if format is False else sifra(res)


def metade(v=0, format=False):
    """
    -> Diminui pela metade o valor de entrada.
    :param v: Valor para dividir na metade.
    :param format: Retorna ou não o valor convertido em moeda.
    :return: Retorna o valor dividido pela metade.
    Criado por Ruannino.
    """
    res = v // 2
    return res if format is False else sifra(res)


def sifra(v=0, s='R$'):
    """
    -> Converte o valor de entrada para o formato de moeda.
    :param v: Valor para converter.
    :param s: Sifra da moeda, por padrão 'R$'.
    :return: Retorna o valor de entrada em formato de moeda.
    Criado por Ruannino.
    """
    return f'{s} {v:.2f}'.replace('.', ',')


def resumo(v=0, pa=0, pr=0):
    """
    -> Trás o resumo de preço com vários parâmetros.
    :param v: Valor para resumo.
    :param pa: Porcentagem de aumento.
    :param pr: Porcentagem de diminuição.
    :return: Retorna uma tabela completa com iterações com o valor digitado.
    Criado por Ruannino.
    """
    print('=' * 40)
    print('RESUMO DE PREÇO'.center(40))
    print('=' * 40)
    print(f'{"Analisado o valor: ":<30}{sifra(v):>10}')
    print(f'{"Dobro do preço: ":<30}{dobro(v, True):>10}')
    print(f'{"A metade do preço: ":<30}{metade(v, True):>10}')
    print(f"Aumentando {pa}% do preço: ".ljust(30) + f"{aumentar(v, pa, True):>10}")
    print(f"Diminuindo {pr}% do preço: ".ljust(30) + f"{aumentar(v, pa, True):>10}")
    print('=' * 40)
