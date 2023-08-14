# Crie um programa que vai ler vários números e colocar em uma lista,
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numbers = []
n_imp = []
n_par = []
while True:
    numbers.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar ? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
for n in range(0, numbers):
    if numbers[n] % 2 == 0:
        n_par.append(numbers(n[:]))
print(numbers)
print(n_imp)
print(n_par)