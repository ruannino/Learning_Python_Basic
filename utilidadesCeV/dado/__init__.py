def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg).replace(',', '.'))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[31mErro! \033[m{entrada} é um preço inváliddo!')
        else:
            valido = True
            return float(entrada)
