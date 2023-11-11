# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
# de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from liber.interface import menu, leia_int, titulo
from time import sleep
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        titulo('Opção1')
    elif resp == 2:
        titulo('Opção2')
    elif resp == 3:
        titulo('Saindo do Sistema - Até logo!')
        break
    else:
        print('\033[31mErro!\033[m Digite uma opção válida!')
    sleep(3)
