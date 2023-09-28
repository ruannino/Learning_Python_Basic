# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - até 9 anos: mirim;
# - até 14 anos: infantil;
# - até 19 anos: júnior;
# - até 20 anos: sênior;
# - acima de 20: master.
from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
if 1 <= idade <= 9:
    print('\033[30mCATEGORIA:\033[m Mirim')
elif 10 <= idade <= 14:
    print('\033[30mCATEGORIA:\033[m Infantil')
elif 15 <= idade <= 19:
    print('\033[30mCATEGORIA:\033[m Júnior')
elif idade == 20:
    print('\033[30mCATEGORIA:\033[m Sênior')
elif 21 <= idade:
    print('\033[30mCATEGORIA:\033[m Master')
else:
    print('\033[31mERRO! digite um ano válido...\033[m')
