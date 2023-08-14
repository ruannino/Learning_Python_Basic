# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numbers = []
while True:
    numbers.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if resposta in 'N':
        break
print(f'Você digitou {len(numbers)} valores')
numbers.sort(reverse=True)
print(f'A lista ordenada descrescente {numbers}')
if 5 in numbers:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
