# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numbers = []
n = 0
pos_five = []
while True:
    numbers.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar ? \033[40m[S/N]\033[m ')).strip().upper()
    if 'N' in continuar:
        break
for n in range(0, len(numbers)):
    if n == 5:
        pos_five.append(n[:])
print(numbers)
print(pos_five)