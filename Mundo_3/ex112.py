# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
# de dados para aceitar apenas valores que sejam monetários.
from utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import leia_dinheiro

n = leia_dinheiro('Digite o preço: R$')
resumo(n, 10, 15)
