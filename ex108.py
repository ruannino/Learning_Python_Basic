# Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores
# como um valor monetário formatado.
from moedas import moeda

v = float(input('Digite o valor do produto: R$ '))
p = int(input('Digite a porcentagem a incrementar: % '))
print(f'{moeda.moeda(v)}')
