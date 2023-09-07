# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. ex.: digite um número: 1834
numero = input('Digite um número entre [0-9999]: ')
numero_formatado = numero.zfill(4)
milhar = numero_formatado[0]
centena = numero_formatado[1]
dezena = numero_formatado[2]
unidade = numero_formatado[3]
print(f'''O milhar: {milhar}
A centena: {centena}
A dezena: {dezena}
A unidade: {unidade}''')
