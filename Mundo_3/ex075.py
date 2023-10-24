# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.  B) Em que posição foi digitado o primeiro valor 3.  C) Quais foram os números
# pares.

numbers = ((int(input('Digite o 1º Valor: '))), (int(input('Digite o 2º Valor: '))),
           (int(input('Digite o 3º Valor: '))), (int(input('Digite o 4º Valor: '))))
print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu primeiro na posição {numbers.index(3) + 1}ª')
else:
    print(f'O Valor 3 não foi digitado')
print(f'Os números pares são: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')

