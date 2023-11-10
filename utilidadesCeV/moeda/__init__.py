def aumentar(v=0, p=0):
    a = v + (p / 100) * v
    return f'R$ {a:.2f}'.replace('.', ',')


def diminuir(v=0, p=0):
    d = v - (p / 100) * v
    return f'R$ {d:.2f}'.replace('.', ',')


def dobro(v=0):
    d = v * 2
    return f'R$ {d:.2f}'.replace('.', ',')


def metade(v=0):
    m = v // 2
    return f'R$ {m:.2f}'.replace('.', ',')
