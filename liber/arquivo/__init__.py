from liber.interface import titulo

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um \033[31mERRO\033[m na criação do arquivo!')
    else:
        print(f'\033[32mArquivo {nome} criado com Sucesso!\033[m')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31mErro!\033[m não consigo ler o arquivo {nome}!')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())