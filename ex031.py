# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas
distancia_viagem = float(input('Qual a distância da viagem em Km: '))
if distancia_viagem <= 200:
    valor_vc = distancia_viagem * 0.50
    print('-' * 40)
    print(f'VIAGEM CURTA'.center(40))
    print('-' * 40)
    print(f'Sua viagem de \033[33m{distancia_viagem}km\033[m. Custará \033[32mR${valor_vc:.2f}\033[m.'.center(40))
    print('-' * 40)
else:
    valor_vl = distancia_viagem * 0.45
    print('-' * 40)
    print(f'VIAGEM LONGA'.center(40))
    print('-' * 40)
    print(f'Sua viagem de \033[33m{distancia_viagem}km\033[m. Custará \033[32mR${valor_vl:.2f}\033[m.'.center(40))
    print('-' * 40)
