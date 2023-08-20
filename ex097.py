# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.   Ex.: escreva('Olá, mundo!') Saída: __ Olá mundo!--  ('~')
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


txt = input('Digite um Título: ')
escreva(txt)git statistics
