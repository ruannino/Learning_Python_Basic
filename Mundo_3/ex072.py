# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

extenso_ingles = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                  'Nineteen', 'Twenty')

while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('\033[31mTente novamente...\033[m', end='')
    print('=' * 40)
    print(f'O número digitado foi o \033[32m{extenso[num]}\033[m')
    print(f'O número digitado em inglês é \033[33m{extenso_ingles[num]}\033[m')
    print('=' * 40)
    while True:
        choice = str(input('Quer continuar ? \033[40m[S/N]\033[m: ')).upper().strip()
        if 'S' in choice or 'N' in choice:
            break
        else:
            print('\033[31mDigite uma opção válida...\033[m', end='')
    if 'N' in choice:
        print('\033[31mEncerrando...\033[m')
        break
