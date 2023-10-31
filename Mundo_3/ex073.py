# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:    A) Apenas os 5 primeiros colocados.   B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfábetica.   D) Em que posição na tabela está o time da Chapecoense.
# 'Corinthians' , 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
# 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Coritiba', 'Avaí',
# 'Ponte Preta', 'Atlético-GO'

tabela = ('Corinthians' , 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
          'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('\033[32m=\033[33m-\033[m' * 40)
print('BRASILEIRÃO'.center(80))
print('\033[32m=\033[33m-\033[m' * 40)
print(f'Lista de times no Brasileirão: {tabela}')
print('\033[32m=\033[33m-\033[m' * 40)
print(f'Os 5 primeiros colocados: {tabela[0:5]}')
print('\033[32m=\033[33m-\033[m' * 40)
print(f'Os 4 últimos colocados: {tabela[-4:]}')
print('\033[32m=\033[33m-\033[m' * 40)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('\033[32m=\033[33m-\033[m' * 40)
print(f'O Chapecoense está na \033[34m{tabela.index("Chapecoense") + 1}ª posição\033[m.')
print('\033[32m=\033[33m-\033[m' * 40)
