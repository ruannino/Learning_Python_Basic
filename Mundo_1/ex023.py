# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. ex.: digite um número: 1834
numero = int(input('Digite um número entre [0-9999]: '))
n = str(numero)
n_formatado = n.zfill(4)
milhar = n_formatado[0]
centena = n_formatado[1]
dezena = n_formatado[2]
unidade = n_formatado[3]
print('Método String')
print(f'''O milhar: {milhar}
A centena: {centena}
A dezena: {dezena}
A unidade: {unidade}''')

m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10
print(f'''O milhar: {m}
A centena: {c}
A dezena: {d}
A unidade: {u}''')
