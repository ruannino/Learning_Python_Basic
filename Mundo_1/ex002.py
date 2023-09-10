# # Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data
# formatada
nome = str(input('Qual seu nome? '))
dia = int(input('Qual o dia do seu nascimento? '))
mes = str(input('Qual o mês do seu nascimento? '))
ano = int(input('Qual o ano em que nasceu? '))
print('~' * 40)
print(f'{"SEU NASCIMENTO":_^40}')
print(f'Nome: \033[32m{nome}\033[m'.center(40))
print(f'Nascimento: \033[32m{dia}/{mes}/{ano}\033[m'.center(40))
print('~' * 40)
