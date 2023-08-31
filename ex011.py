# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
rendimento = area / 2
print('-' * 20)
print('RENDIMENTO DE TINTA'.center(20))
print('-' * 20)
print(f'Largura: {largura:.2f}mt')
print(f'Altura: {altura:.2f}mt')
print(f'Área: {area:.2f}mt²')
print('-' * 20)
print(f'Tinta: {rendimento:.2f}Lt')
print('-' * 20)
