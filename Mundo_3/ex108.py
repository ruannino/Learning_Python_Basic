# Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores
# como um valor monetário formatado.
from utilidadesCeV.moeda import aumentar, diminuir, dobro, metade, sifra

n = float(input('Digite o preço: R$'))
print(f'O sobro de {sifra(n)} é {sifra(dobro(n))}')
print(f'A metade de {sifra(n)} é {sifra(metade(n))}')
print(f'Aumento de {sifra(n)} em 10% é {sifra(aumentar(n, 10))}')
print(f'Diminuindo {sifra(n)} em 20% é {sifra(diminuir(n, 20))}')
