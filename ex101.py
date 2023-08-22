# crie um programa que tenha uma função chamada voto() que vai receber como parâmentro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        print(f'Um pessoa com {idade} anos. tem o voto: Negado.')
    elif 18 > idade >= 16 or idade >= 65:
        print(f'Um pessoa com {idade} anos. tem o voto: Opcional.')
    else:
        print(f'Um pessoa com {idade} anos. tem o voto: Obrigatório.')


# Programa Principal
n = int(input('Digite o ano de nascimento: '))
voto(n)
