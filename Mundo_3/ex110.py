# Adicione ao módulo moeda.py, criado nos exercícios anteriores, uma função chamada resumo(), que mostre
# na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from utilidadesCeV.moeda import resumo

n = float(input('Digite o preço: R$'))
resumo(n, 10, 15)
