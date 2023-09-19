# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
numero = int(input('Digite um número: '))
print('\033[33m=\033[m' * 20)
print(f'TABUADA DO {numero}'.center(20))
print('\033[33m=\033[m' * 20)
for n in range(0, 11):
    print(f'{n} x {numero} = {n * numero}'.center(20))
print('\033[33m=\033[m' * 20)
