# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo
# funcionando.
from utilidadesCeV import moeda

n = float(input('Digite o preço: R$'))
moeda.resumo(n, 10, 15)
