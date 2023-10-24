# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

table_products = ('Laranja', 3, 'Limão', 1.5, 'Melância', 7, 'Uva', 5, 'Morango', 12.5, 'Kiwi', 8,
                  'Mamão', 2.5, 'Banana', 6, 'Maçã', 0.8, 'Abacaxi', 5.8 )
print('-' * 40)
print(f'{"PRODUCT LIST":^40}')
print('-' * 40)
for product in range(0, len(table_products)):
    if product % 2 == 0:
        print(f'{table_products[product]:.<30}', end='')
    else:
        print(f'R${table_products[product]:>7.2f}')
print('-' * 40)