# Reescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leia_float()
# com a mesma funcionalidade.
from utilidadesCeV.dado import leia_int, leia_float

n = leia_int('Digite um número Inteiro: ')
print(f'o valor digitado foi {n}')

f = leia_float('Digite um número Real: ')
print(f'o valor digitado foi {f}')
