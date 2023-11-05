# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.   Ex.: escreva('Olá, mundo!') Saída: __ Olá mundo!--  ('~')
def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva('SER DEV É SE COMPROMETER')
escreva('TAMO NA LUTA')
escreva('BIT')
