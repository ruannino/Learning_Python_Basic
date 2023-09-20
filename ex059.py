# Crie um programa que leia dois valores e mostre um menu na tela:
# 1: somar
# 2: multiplicar
# 3: maior
# 4: novos números
# 5: sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso:
num1 = num2 = 0
opcao =
print('=' * 40)
print('=' * 40)
while opcao != 5:
    while opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    print('Escolha uma opção para realizar!')
    opcao = int(input('[1] Somar:'
                      '\n[2] Multiplicar:'
                      '\n[3] Maior:'
                      '\n[4] Novos Números:'
                      '\n[5] Sair do Programa:'))
    print('=' * 40)
    if opcao == 1:
        print(f'SOMAR:  {num1} + {num2} = {num1 + num2}.')
        print('=' * 40)
    elif opcao == 2:
        print(f'MULTIPLICAR:  {num1} + {num2} = {num1 + num2}.')
        print('=' * 40)
    elif opcao == 3:
        if num1 > num2:
            print(f'MAIOR:  {num1} > {num2}, logo {num1} é o MAIOR.')
            print('=' * 40)
        else:
            print(f'MAIOR:  {num2} > {num1}, logo {num2} é o MAIOR.')
            print('=' * 40)
