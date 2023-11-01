# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.  B) Em que posição foi digitado o primeiro valor 3.  C) Quais foram os números
# pares.
tres = pares = 0
print('\033[31m=\033[m' * 50)
print('ENCONTRAR NÚMEROS EM TUPLA'.center(50))
print('\033[31m=\033[m' * 50)
valores = ((int(input('Digite um valor de \033[40m[0 a 10]:\033[m'))),
           (int(input('Digite um valor de \033[40m[0 a 10]:\033[m'))),
           (int(input('Digite um valor de \033[40m[0 a 10]:\033[m'))),
           (int(input('Digite um valor de \033[40m[0 a 10]:\033[m'))))
print('\033[31m-\033[m' * 50)
print('RESULTADO'.center(50))
for n in valores:
    if n == 3 and tres == 0:
        tres = valores.index(n) + 1
print(f'O valor 9 apareceu: {valores.count(9)} vezes.')
if tres > 0:
    print(f'O valor 3 apareceu a primeira vez na {tres}ª posição.')
else:
    print(f'O valor 3 não foi digitado nenhuma vez.')
print(f'Valores pares digitados: ', end='')
for v in valores:
    if v % 2 == 0:
        print(f'{v} ', end='')
        pares += 1
if pares == 0:
    print('Nenhum')
print()
print('\033[31m-\033[m' * 50)
