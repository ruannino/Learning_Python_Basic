# Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar semelhante a função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.    Ex.: n = leiaInt('Digite um n')
def leia_int(msn):
    valor = 0
    ok = False
    while True:
        num = str(input(msn))
        if num.isnumeric():
            valor = num
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido...\033[m')
        if ok:
            break
    return valor


n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}.')
