def aumentar(valor=0, porcentagem_a=0, formato=False):
    dif = valor + valor * (porcentagem_a / 100)
    return dif if formato is False else moeda(dif)


def diminuir(valor=0, porcentagem_r=0, formato=False):
    dif = valor - valor * (porcentagem_r / 100)
    return dif if formato is False else moeda(dif)


def dobro(valor=0, formato=False):
    d = valor * 2
    return d if formato is False else moeda(d)


def metade(valor=0, formato=False):
    m = valor / 2
    return m if formato is False else moeda(m)


def moeda(valor=0, sifra='R$'):
    return f'{sifra}{valor:<8.2f}'.replace('.', ',')


def resumo(valor=0, porcentagem_a=10, porcentagem_r=5):
    print('-' * 40)
    print('REDUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Com {porcentagem_a}% aumento: \t{aumentar(valor, porcentagem_a, True)}')
    print(f'Com {porcentagem_r}% redução: \t{diminuir(valor, porcentagem_r, True)}')
    print('-' * 40)
