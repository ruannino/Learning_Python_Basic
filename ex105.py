# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# ->Quantidade de notas ->A maior nota ->A menor nota ->A média da turma ->A situação(opcional)
# Adiciona também docstrings da função


def notas(* nt, sit=False):
    """
    -> Função realiza análise das notas e situação da turma,
    coloca todos os dados em um dicionário.
    :param nt: recebe as notas da turma.
    :param sit: Opcional se deseja ou não mostrar a situação da turma.
    :return: Um dicionário com informações detalhadas da turma.
    """
    turma = dict()
    turma['Total'] = len(nt)
    maior = menor = nt[0]
    for n in nt:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    turma['maior'] = maior
    turma['menor'] = menor
    soma = sum(nt)
    turma['media'] = soma / len(nt)

    if sit:
        if turma['media'] >= 7:
            turma['situação'] = 'Boa'
        elif 5 <= turma['media'] < 7:
            turma['situação'] = 'Razoável'
        else:
            turma['situação'] = 'Péssima'
    print(turma)


notas(2.5, 5, 7, 9, sit=True)
notas(2.5, 5, 3, 9, sit=True)
