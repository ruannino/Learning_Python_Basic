# Crie um programa que vai ler vários números e colocar em uma lista,
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numbers = []
n_imp = []
n_par = []
while True:
    numbers.append(int(input('Digite um número: ')))
    mensagem = str(input('Quer continuar ? [S/N]')).strip().upper()
    if mensagem in 'N':
        break
for c in numbers:
    if c % 2 == 0:
        n_par.append(c)
        c += 1
    else:
        n_imp.append(c)
print(numbers)
print(n_imp)
print(n_par)
