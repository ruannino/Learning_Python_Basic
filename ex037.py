# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 2 para hexadecimal.
num = int(input('Digite um número para conversão: '))
op = int(input('''Qual base de conversão:
\033[40m[ 1 ]\033[m - Binário;
\033[40m[ 2 ]\033[m - Octal;
\033[40m[ 3 ]\033[m - Hexadecimal;
        Sua opção ->'''))
if op == 1:
    print(f'O número \033[33m{num}\033[m em Binário -> \033[33m{bin(num)[2:]}\033[m')
elif op == 2:
    print(f'O número \033[33m{num}\033[m em Octal -> \033[33m{oct(num)[2:]}\033[m')
elif op == 3:
    print(f'O número \033[33m{num}\033[m em Hexadecimal -> \033[33m{hex(num)[2:]}\033[m')
else:
    print(f'\033[31mERRO! você digitou uma opção inválida!\033[m')
