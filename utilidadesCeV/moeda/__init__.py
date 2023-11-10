def aumentar(v=0, p=0, format=False):
    res = v + (p / 100) * v
    return res if format is False else sifra(res)


def diminuir(v=0, p=0, format=False):
    res = v - (p / 100) * v
    return res if format is False else sifra(res)


def dobro(v=0, format=False):
    res = v * 2
    return res if format is False else sifra(res)


def metade(v=0, format=False):
    res = v // 2
    return res if format is False else sifra(res)


def sifra(v=0, s='R$'):
    return f'{s} {v:.2f}'.replace('.', ',')


def resumo(v=0, pa=0, pr=0):
    print('=' * 40)
    print('RESUMO DE PREÇO'.center(40))
    print('=' * 40)
    print(f'{"Analisado o valor: ":<30}{sifra(v):>10}')
    print(f'{"Dobro do preço: ":<30}{dobro(v, True):>10}')
    print(f'{"A metade do preço: ":<30}{metade(v, True):>10}')
    print(f"Aumentando {pa}% do preço: ".ljust(30) + f"{aumentar(v, pa, True):>10}")
    print(f"Diminuindo {pr}% do preço: ".ljust(30) + f"{aumentar(v, pa, True):>10}")
    print('=' * 40)
