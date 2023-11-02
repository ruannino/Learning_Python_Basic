# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois mostrar, para cada palavra, quais são as suas vogais.

conjunto_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
                     'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in conjunto_palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
