# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - média abaixo de 5.0: reprovado;
# - média entre 5.0 e 6,9: recuperação;
# - média 7.0 ou superior: aprovado;
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Média: \033[34m{media:.1f}\033[m. \033[32mAPROVADO!\033[m')
elif 5 <= media <= 6.9:
    print(f'Média: \033[34m{media:.1f}\033[m. \033[33mRECUPERAÇÃO!\033[m')
else:
    print(f'Média: \033[34m{media:.1f}\033[m. \033[31mREPROVADO!\033[m')
