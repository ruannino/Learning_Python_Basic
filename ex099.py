# Faça um programa que tenha uma funcão chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.
def maior(* num):
    for n in num:
        if n == 0:
            maior = num
        elif n > maior:
            maior = num


maior(maior)