# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expr = str(input('Digite a sua expressão: '))
par = []
for sim in expr:
    if sim == '(':
        par.append('(')
    elif sim == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão tem erros!')


