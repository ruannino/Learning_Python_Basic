# Finalizando o projeto
from liber.interface import *
from liber.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        ler_arquivo(arq)
    elif resp == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leia_int('Idade: ')
        novo_cadastro(arq, nome, idade)
    elif resp == 3:
        titulo('Saindo do Sistema - Até logo!')
        break
    else:
        print('\033[31mErro!\033[m Digite uma opção válida!')
    sleep(3)
