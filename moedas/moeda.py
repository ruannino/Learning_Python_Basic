def aumentar(valor, porcentagem=0):
    dif = valor * (porcentagem / 100)
    a_valor = valor + dif
    return a_valor


def diminuir(valor, porcentagem=0):
    dif = valor * (porcentagem / 100)
    d_valor = valor - dif
    return d_valor


def dobro(valor):
    d = valor * 2
    return d


def metade(valor):
    m = valor / 2
    return m


def moeda(msg):
    mon = float(msg)
    return f'R$ {mon:.2f}'
