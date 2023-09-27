# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.
total = cont = maior = menor = 0
option = ''
while 'N' not in option:
    n = int(input('Digite um número: '))
    option = str(input('Quer continuar \033[42m[S/N]\033[m: ')).strip().upper()
    while option[0] != 'S' and option[0] != 'N':
        option = str(input('\033[31mERRO! digite \033[33m"S"\033[m ou \033[33m"N"\033[m: ')).strip().upper()
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    cont += 1
    total += n
media = total / cont
print('-' * 60)
print('RESULTADOS'.center(60))
print('-' * 60)
print(f'''A \033[33mmédia\033[m total dos \033[33m{cont}\033[m valores digitados é \033[33m{media:.2f}\033[m;
O \033[31mmaior\033[m valor digitado foi \033[31m{maior}\033[m;
O \033[32mmenor\033[m valor digitado foi \033[32m{menor}\033[m.''')
print('-' * 60)
