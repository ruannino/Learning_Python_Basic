# Faça um mini-sistema que utilize o INTERACTIVE HELP do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.    OBS.: use cores.
from time import sleep


c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelha
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;37m'      # 6 - branco
     )


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        sleep(2)
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
