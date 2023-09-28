# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, e acordo com a tabela abaixo:
# - abaixo de 18.5: abaixo do peso;
# - entre 18.5 e 25: peso ideal;
# - 25 até 30: sobrepeso;
# - 30 até 40: obesidade;
# - acima de 40: obesidade mórbida.
peso = float(input('Informe o peso: (kg)'))
altura = float(input('Informe a altura: (m)'))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'Seu IMC \033[34m{IMC:.2f}\033[m. Você está abaixo do peso.')
elif 18.5 <= IMC <= 24.9:
    print(f'\033[32mSeu IMC {IMC:.2f}. Você está saudável.\033[m')
elif 25 <= IMC <= 29.9:
    print(f'\033[35mSeu IMC {IMC:.2f}. Você está com sobrepeso.\033[m')
elif 30 <= IMC <= 34.9:
    print(f'\033[33mSeu IMC {IMC:.2f}. Você está com obesidade grau I.\033[m')
elif 35 <= IMC <= 39.9:
    print(f'\033[33mSeu IMC {IMC:.2f}. Você está com obesidade grau II (severa).\033[m')
elif IMC >= 40:
    print(f'\033[31mSeu IMC {IMC:.2f}. Você está com obesidade grau III (mórbida).\033[m')
