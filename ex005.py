# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
n = int(input('Digite um número: '))
print(f'O numero digitado foi: \033[32m{n}\033[m\n'
      f'Seu antecessor é : \033[32m{n - 1}\033[m\n'
      f'Seu sucessor é : \033[32m{n + 1}\033[m')
