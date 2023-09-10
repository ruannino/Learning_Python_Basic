# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
# Verificando os menores:
# Verificando os maiores:
# Printando os resultados onde a variável parou:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = menor = n1
if n2 > n1 and n3 < n2:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n2
print(f'O \033[33mMENOR\033[m número digitado foi \033[33m{menor}\033[m, '
      f'e o \033[33mMAIOR\033[m foi \033[33m{maior}\033[m')
