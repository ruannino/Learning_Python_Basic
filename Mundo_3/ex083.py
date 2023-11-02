# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = []
sim = []
exp.append(str(input('Digite sua expressão: ')).strip())
for ex in exp:
    for e in ex:
        if e == '(':
            sim.append(e)
        elif e == ')':
            sim.append(e)
if len(sim) % 2 == 0:
    print(f'A expressão {exp}. VÁLIDA!')
else:
    print(f'A expressão {exp}. INVÁLIDA!')
