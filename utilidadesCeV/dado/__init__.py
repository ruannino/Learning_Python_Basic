def leia_dinheiro(msg):
    """
    -> Verifica os valores de moeda e válida os dados.
    :param msg: Recebe o valor.
    :return: Retorna o valor, já validado e convertido.
    Criado por Ruannino.
    """
    valido = False
    while not valido:
        entrada = str(input(msg).replace(',', '.'))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[31mErro! \033[m{entrada} é um preço inváliddo!')
        else:
            valido = True
            return float(entrada)


def leia_int():
    """
    -> Verifica se o input é númerico.
    :return: Apenas caso o input seja númerico.
    Criada por Ruannino.
    """
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            print(f'Você digitou o número \033[32m>>>\033[m {num}!')
            break
        else:
            print('\033[31mErro!\033[m Digite um número válido!')
