# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.
def area(larg, comp):
    s = larg * comp
    print(f'A área do terreno com {larg:.2f}x{comp:.2f}.'.center(45))
    print(f'Total de área de {s}m².'.center(45))


print('=-' * 23)
print('{:^46}'.format("TERRENO EM M²"))
print('=-' * 23)
print()
la = float(input('=> Digite a largura do terreno: '))
co = float(input('=> Digite o comprimento do terreno: '))
print()
area(la, co)
print('=-' * 23)
