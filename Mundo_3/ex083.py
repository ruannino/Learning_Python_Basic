# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = input('Digite sua expressão: ')
sim = []
for e in exp:
    if e == '(':
        sim.append(e)
    elif e == ')':
        if not sim:
            sim.append(e)
        elif sim[-1] == '(':
            sim.pop()
if not sim:
    print(f'A expressão \033[33m{exp}\033[m é \033[32mVÁLIDA!\033[m')
else:
    print(f'A expressão \033[33m{exp}\033[m é \033[31mINVÁLIDA!\033[m')
