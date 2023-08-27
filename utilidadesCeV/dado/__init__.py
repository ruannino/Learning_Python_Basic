def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


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
        else:
            return num


def leia_float(msn):
    while True:
        try:
            num = float(input(msn))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número Real válido...\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num
