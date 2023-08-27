def leia_int(msn):
    while True:
        try:
            num = int(input(msn))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número Inteiro válido...\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
            break
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[32mSua Opção: \033[m')
    return opc
