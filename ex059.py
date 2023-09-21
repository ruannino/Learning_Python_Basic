# Crie um programa que leia dois valores e mostre um menu na tela:
# 1: somar
# 2: multiplicar
# 3: maior
# 4: novos números
# 5: sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso:
from time import sleep
opcao = 0
print('=' * 40)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while opcao != 5:
    print('Escolha uma opção para realizar!')
    opcao = int(input('\033[40m[1]\033[m Somar:'
                      '\n\033[40m[2]\033[m Multiplicar:'
                      '\n\033[40m[3]\033[m Maior:'
                      '\n\033[40m[4]\033[m Novos Números:'
                      '\n\033[40m[5]\033[m Sair do Programa:'))
    print('=' * 40)
    if opcao == 1:
        print(f'\033[32mSOMAR: \033[m{num1} + {num2} = {num1 + num2}.')
        print('=' * 40)
    elif opcao == 2:
        print(f'\033[32mMULTIPLICAR: \033[m{num1} x {num2} = {num1 * num2}.')
        print('=' * 40)
    elif opcao == 3:
        if num1 > num2:
            print(f'\033[32mMAIOR:\033[m {num1} > {num2}, logo {num1} é o MAIOR.')
            print('=' * 40)
        else:
            print(f'\033[32mMAIOR:\033[m {num2} > {num1}, logo {num2} é o MAIOR.')
            print('=' * 40)
    elif opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Preparando para sair...', end='')
        sleep(1)
    else:
        print('\033[31mERRO! Opção inválida, tente novamente...\033[m')
        print('=' * 40)
    sleep(1)
print('\033[31mENCERRANDO...\033[m')
