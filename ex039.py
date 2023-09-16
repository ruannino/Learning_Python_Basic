# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar;
# - Se já passou do tempo do alistamento;
# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
if idade == 18:
    print(f'Um jovem de \033[32m{idade}\033[m anos. Deve se alistar imediatamente!')
elif idade > 18:
    diferenca_maior = idade - 18
    print(f'Com \033[31m{idade}\033[m anos. Já passou \033[31m{diferenca_maior}\033[m anos do seu alistamento!')
else:
    diferenca_menor = 18 - idade
    print(f'Com \033[35m{idade}\033[m anos. Faltam \033[35m{diferenca_menor}\033[m anos para o seu alistamento!')
