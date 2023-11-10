# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.
from utilidadesCeV.moeda import aumentar, diminuir, dobro, metade, sifra

n = float(input('Digite o preço: R$'))
print(f'O sobro de {sifra(n)} é {dobro(n, True)}')
print(f'A metade de {sifra(n)} é {metade(n, True)}')
print(f'Aumento de {sifra(n)} em 10% é {aumentar(n, 10, True)}')
print(f'Diminuindo {sifra(n)} em 20% é {diminuir(n, 20, True)}')
