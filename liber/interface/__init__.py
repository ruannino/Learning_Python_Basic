def leia_int(msg):
    """
    -> Verifica se o valor numérico inserido é inteiro.
    :param msg: Inseri o valor.
    :return: Retorna o valor quando o valor é inteiro.
    Criado por Ruannino.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro!\033[m Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('\033[33mEntrada de dados interropida pelo usuário!\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(f'{msg}'.center(42))
    print(linha())

def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c} - \033[34m{i}\033[m')
        c += 1
    print(linha())
    op = leia_int('\033[32mSua opção:\033[m ')
    return op