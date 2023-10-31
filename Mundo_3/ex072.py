# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostrá-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

extenso_ingles = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                  'Nineteen', 'Twenty')
while True:
    print('\033[34m=\033[m' * 40)
    print('NÚMERO EM EXTENSO/INGLÊS'.center(40))
    print('\033[34m=\033[m' * 40)
    while True:
        num = int(input('Digite um número entre \033[32m0\033[m e \033[32m20\033[m:'))
        if 0 <= num <= 20:
            break
        else:
            print('\033[31mTente novamente...\033[m', end='')
    print('RESPOSTA'.center(40, '-'))
    print(f'Seu número por extenso é \033[32m{extenso[num]}\033[m.')
    print(f'Seu número em inglês é \033[33m{extenso_ingles[num]}\033[m.')
    opcao = str(input('Quer continuar ? \033[40m[S/N]\033[m ')).strip().upper()
    if opcao[0] == 'N':
        print('\033[31mEncerrando...\033[m')
        break
    elif opcao[0] == 'S':
        print('\033[33mReiniciando...\033[m')
    else:
        print('\033[31mErro no sistema...\033[m')
        break
print('-' * 40)
