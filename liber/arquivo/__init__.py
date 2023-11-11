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
    except Exception:
        print(f'\033[31mErro!\033[m não consigo ler o arquivo {nome}!')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def novo_cadastro(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[31mErro!\033[m não consigo abrir o arquivo {arquivo}!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[31mErro!\033[m não consigo escrever no arquivo {arquivo}!')
        else:
            print(f'\033[32mRegistro de {nome} adicionado com sucesso!\033[m')
            a.close()
