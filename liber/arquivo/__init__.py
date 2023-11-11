from liber.interface import titulo


def arquivo_existe(nome):
    """
    -> Verifica se um arquivo existe ou não.
    :param nome: Nome do arquivo.
    :return: Verdadeiro se o arquivo foi encontrado ou Falso se o arquivo não foi encontrado.
    Criado por Ruannino.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto.
    :param nome: Recebe o nome do arquivo a ser criado.
    :return: Criação de um arquivo txt.
    Criado por Ruannino.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um \033[31mERRO\033[m na criação do arquivo!')
    else:
        print(f'\033[32mArquivo {nome} criado com Sucesso!\033[m')


def ler_arquivo(nome):
    """
    -> Faz a leitura de uma arquivo e o ordena em um layout.
    :param nome: Recebe o nome do arquivo a ser lido.
    :return: Imprime os dados do arquivo em um layout ordenado.
    Criado por Ruannino.
    """
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
    """
    -> Cadastra dados de nome e idade de uma pessoa em um arquivo de texto.
    :param arquivo: Nome do arquivo de cadastramento.
    :param nome: Nome para inserir no cadastro.
    :param idade: Idade para inserir no cadastro.
    :return: Cadastro dos dados no arquivo de cadastramento.
    Criado por Ruannino.
    """
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
