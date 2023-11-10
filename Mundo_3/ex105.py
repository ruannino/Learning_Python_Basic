# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# ->Quantidade de notas ->A maior nota ->A menor nota ->A média da turma ->A situação(opcional)
# Adiciona também docstrings da função
def notas(*n, sit=False):
    """
    -> Executa a leitura de uma ou mais notas e distribui informações dentro de um dicionário.
    :param n: Recebe as notas dentro do parâmetro
    :param sit: Define opcionalmente se será exibida ou não a situação.
    :return: Retorna um dicionário com várias informações como: total de notas,
            maior nota, menor nota, média e situação(opcional).
    Criada por Ruannino.
    """
    ficha = dict()
    ficha['Total'] = len(n)
    ficha['Maior'] = max(n)
    ficha['Menor'] = min(n)
    ficha['Média'] = sum(n) / len(n)
    if sit:
        if ficha['Média'] >= 7:
            ficha['Situação'] = 'BOA'
        elif 5 <= ficha['Média'] < 7:
            ficha['Situação'] = 'RAZOÁVEL'
        else:
            ficha['Situação'] = 'RUIM'
    return ficha


# Programa Principal
print(notas(3.4, 6.7, 4.5, sit=True))
print(notas(10, 9.7, 8.5, sit=True))
print(notas(4, 5.7, 7.5))
