# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
# de dados para aceitar apenas valores que sejam monetários.
from utilidadesCeV import moeda
from utilidadesCeV import dado

v = dado.leia_dinheiro('Digite o valor do produto: R$ ')
moeda.resumo(v, 25, 22)
