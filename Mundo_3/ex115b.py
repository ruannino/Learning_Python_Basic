# Criando um menu em Python
from liber.interface import menu, titulo
from liber.arquivo import arquivo_existe, criar_arquivo, ler_arquivo
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        ler_arquivo(arq)
    elif resp == 2:
        titulo('Opção2')
    elif resp == 3:
        titulo('Saindo do Sistema - Até logo!')
        break
    else:
        print('\033[31mErro!\033[m Digite uma opção válida!')
    sleep(3)
