# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
algo = input('Digite algo: ')
print(type(algo))
print(f'É um valor numérico ? {algo.isnumeric()}')
# Retorna True se todos os caracteres na string forem numéricos
print(f'É um valor Alfabético ? {algo.isalpha()}')
# Retorna True se todos os caracteres na string forem alfabéticos
print(f'O valor está em Caixa Alta? {algo.isupper()}')
# Retorna True se todos os caracteres na string estiverem em caixa alta
print(f'O valor está em Caixa Baixa ? {algo.islower()}')
# Retorna True se todos os caracteres na string estiverem em caixa baixa
print(f'É um valor numérico ? {algo.isalnum()}')
# Retorna True se a string for alfanumérica, ou seja, se todos os caracteres na string forem letras ou dígitos
print(f'É um valor numérico ? {algo.isdigit()}')
# Retorna True se todos os caracteres na string forem dígitos
print(f'É um valor numérico ? {algo.isdecimal()}')
# Retorna True se todos os caracteres na string forem dígitos decimais (0-9)
print(f'É um valor numérico ? {algo.isascii()}')
# Retorna True se todos os caracteres na string forem caracteres ASCII
# (ou seja, caracteres que podem ser representados em codificação ASCII).
print(f'É um valor numérico ? {algo.isprintable()}')
# Retorna True se todos os caracteres na string forem imprimíveis, ou seja,
# caracteres que podem ser impressos na tela, como letras, números e símbolos.
print(f'É um valor numérico ? {algo.isspace()}')
# Retorna True se todos os caracteres na string forem espaços em branco (espaço, tabulação, nova linha, etc.)
print(f'É um valor numérico ? {algo.isidentifier()}')
# Retorna True se a string for um identificador válido em Python. Um identificador válido em Python
# segue regras específicas, como começar com uma letra ou sublinhado e conter apenas letras, dígitos ou sublinhados.
print(f'É um valor numérico ? {algo.istitle()}')
# Retorna True se a string estiver em formato de título, ou seja, se a primeira
# letra de cada palavra na string estiver em maiúscula e as outras em minúscula. Caso contrário, retorna False.
