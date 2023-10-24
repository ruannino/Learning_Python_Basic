# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
# de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from liber.interface import *
from liber.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if detecta_arquivo(arq):
    print('\033[32mArquivo encontrado com sucesso!\033[m')
else:
    print('\033[31mArquivo não encontrado!\033[m')
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver PessoasCadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistem'])
    if resposta == 1:
        # Opção de Listar o conteúdo de um arquivo!
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
