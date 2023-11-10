# Reescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leia_float()
# com a mesma funcionalidade.
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


def leia_float(txt):
    """
    -> Verifica se o valor numérico inserido é real.
    :param txt: Inseri o valor.
    :return: Retorna o valor quando o valor é real.
    Criado por Ruannino.
    """
    while True:
        try:
            num = float(input(txt))
        except (TypeError, ValueError):
            print('\033[31mErro!\033[m Digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print('\033[33mEntrada de dados interropida pelo usuário!\033[m')
            return 0
        else:
            return num


num = leia_int('Digite um valor inteiro: ')
n = leia_float('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num} e o valor real foi {n}')
