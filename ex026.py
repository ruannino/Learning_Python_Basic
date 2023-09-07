# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
# Faça um programa que leia uma frase qualquer:
# Tamanho total da string (só porque eu quero mesmo):
# Quantas vezes aparece a letra "a":
# Em que posição ela aparece a primeira vez:
# Em que posição ela aparece a última vez:
frase = str(input('Digite uma frase qualque: '))
print(f'Frase = {frase}')
print(f'Tamanho da frase = {len(frase)}')
print(f'A letra "a" apareceu {frase.count("a")} vezes')
print(f'A letra "a" apareceu a primeira vez na porsição {frase.find("a")}.')
