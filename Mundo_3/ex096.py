# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.
def area(c, l):
    tot = com * lar
    print(f'O terreno tem \033[32m{tot:.2f} m²\033[m.')


# Programa Principal
print('\033[34m-\033[m' * 30)
print('MEDIDOR DE TERRENO'.center(30))
print('\033[34m-\033[m' * 30)
com = float(input('Comprimento:  ').replace(',', '.'))
lar = float(input('Largura:  ').replace(',', '.'))
area(com, lar)
print('\033[34m-\033[m' * 30)
