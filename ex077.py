# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois mostrar, para cada palavra, quais são as suas vogais.

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for snippet in words:
    print(f'\nNa palavra {snippet.upper()} temos', end=' ')
    for letter in snippet:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
