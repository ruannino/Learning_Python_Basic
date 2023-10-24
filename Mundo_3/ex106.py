# Faça um mini-sistema que utilize o INTERACTIVE HELP do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.    OBS.: use cores.
from time import sleep
c = ('\033[m',    # [0] sem cor
     '\033[41m',  # [1] vermelha
     '\033[42m',  # [2] verde
     '\033[43m',  # [3] amarelo
     '\033[44m',  # [4] azul
     '\033[45m',  # [5] roxo
     '\033[40m'   # [6] preto
     )


def ajuda(com):
    sleep(1)
    titulo(f'Acessando manual do comando {com}', 4)
    print(c[6])
    sleep(1)
    help(com)
    print(c[0])


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sleep(0.5)
titulo('ATÉ LOGO!', 1)
