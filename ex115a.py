# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
# de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from liber.interface import *
from time import sleep

while True:
    resposta = menu(['Ver PessoasCadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistem'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)

