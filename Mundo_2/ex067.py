# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número: '))
    cont = 0
    if num < 0:
        print('\033[31m=\033[m' * 35)
        print('\033[31m > Encerrando...\033[m'.center(30))
        break
    else:
        print('\033[33m=\033[m' * 35)
        print(f'\033[32m*\033[33m== \033[mA TABUADA DO NÚMERO \033[32m{num} \033[33m==\033[32m*\033[m'.center(35))
        print('\033[33m=\033[m' * 35)
        while cont < 10:
            result = cont * num
            print(f'{cont} \033[32mx\033[m {num} \033[32m=\033[m {result}'.center(45))
            cont += 1
    print('\033[33m=\033[m' * 35)
print('\033[31m=\033[m' * 35)
