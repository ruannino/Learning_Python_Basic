# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:    A) Apenas os 5 primeiros colocados.   B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfábetica.   D) Em que posição na tabela está o time da Chapecoense.
# 'Corinthians' , 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
# 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Coritiba', 'Avaí',
# 'Ponte Preta', 'Atlético-GO'

tabela = ('Corinthians' , 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
          'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('TABELA BRASILEIRÃO')
print('=-' * 50)
print(f'A tabela completa do brasileirão: {tabela}')
print('=-' * 50)
print(f'Os #05 primeiros colocados são: {tabela[0:5]}')
print('=-' * 50)
print(f'Os #04 últimos colocados são: {tabela[-4:]}')
print('=-' * 50)
print(f'Os times em ordem alfábetica: {sorted(tabela)}')
print('=-' * 50)
print(f'O Chapecoese está na posição: {tabela.index("Chapecoense")+1}ª')
print('=-' * 50)
print('Encerrando...')