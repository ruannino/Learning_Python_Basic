# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase qualque: ')).strip()
print(f'Frase = {frase}')
print(f'Tamanho da frase = {len(frase)}')
print(f'A letra "a" apareceu {frase.upper().count("A")} vezes')
print(f'A letra "a" apareceu a primeira vez na porsição {frase.upper().find("A") + 1}.')
print(f'A letra "a" apareceu a última vez na porsição {frase.upper().rfind("A") + 1}.')
