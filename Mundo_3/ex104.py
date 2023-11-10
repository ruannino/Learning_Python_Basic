# Crie um programa que tenha uma função chamada leia_int(), que vai funcionar semelhante a função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico. Ex.: n = leiaInt('Digite um n')
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


# Programa Principal
leia_int()
