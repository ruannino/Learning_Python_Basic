# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro? '))
print('-' * 40)
print('\033[31mVocê foi multado!\033[m'.center(40) if velocidade > 80
      else '\033[32mContinue dirigindo em segurança!\033[m'.center(40))
print('-' * 40)
if velocidade > 80:
    multa = velocidade - 80
    multa_total = multa * 7
    print(f'\033[31mVocê foi multado em \033[32mR${multa_total:.2f}\033[m.')
    print('-' * 40)
