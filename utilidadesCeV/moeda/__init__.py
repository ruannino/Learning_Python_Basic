def aumentar(v=0, p=0):
    res = v + (p / 100) * v
    return res


def diminuir(v=0, p=0):
    res = v - (p / 100) * v
    return res


def dobro(v=0):
    res = v * 2
    return res


def metade(v=0):
    res = v // 2
    return res


def sifra(v=0, s='R$'):
    return f'{s} {v:.2f}'.replace('.', ',')
