# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número: '))
    cont = 0
    if num < 0:
        print('\033[31mEncerrando...\033[m')
        break
    else:
        print(f'\033[31m+\033[32m==\033[33mTABUADA DO \033[31m[{num}]\033[32m ==\033[31m+\033[m')
        while cont <= 10:
            result = num * cont
            print(f'    {num} \033[32mx\033[m {cont} \033[32m=\033[m {result}')
            cont += 1
        print('\033[33m=\033[m' * 20)
