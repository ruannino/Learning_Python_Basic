# crie um programa que tenha uma função chamada voto() que vai receber como parâmentro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(a):
    """
    -> Verifica a idade do usuário e retorna a situação de voto.
    :param a: Ano de nascimento do usuário.
    :return: Retorna a situação conforme a idade do usuário. [Negado, Opcional ou Obrigatório]
    Criada por Ruannino.
    """
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'Um cidadão com {idade} anos | Voto: \033[31mNegado!\033[m'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Um cidadão com {idade} anos | Voto: \033[32mOpcional!\033[m'
    else:
        return f'Um cidadão com {idade} anos | Voto: \033[33mObrigatório!\033[m'


# Programa Principal
print('\033[32m=\033[33m=\033[m' * 20)
print(f'\033[32m{"SISTEMA DE VOTO":^40}\033[m')
print('\033[32m=\033[33m=\033[m' * 20)
nasc = int(input('Qual seu ano de nascimento ? '))
print(voto(nasc))
print('\033[32m=\033[33m=\033[m' * 20)
