# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)  # pela pow(n(1/2)) ou pela biblioteca math.sqrt(num)
print(f'O número {num:.0f}, seu dobro {dobro:.0f},'
      f'seu triplo {triplo:.0f}, e sua raiz quadrada {raiz:.0f}.')
