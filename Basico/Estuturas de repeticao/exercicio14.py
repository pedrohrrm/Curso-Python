'''Escreva um algoritmo que leia números inteiros via teclado. Somente valores positivos devem ser aceitos pelo programa.
Ao final da execução, informe a média dos valores digitados. Realize a implementação com as instruções break e continue, 
e trabalhe com operações lógicas Truthy e Falsey. Não esqueça de empregar também operadores especiais de atribuição.'''
num = 0
soma = 0
qtd = 0
media = 0
while True:
    num = int(input('Digite um número inteiro maior que zero: '))
    if not num:
        print('Número negativo digitado. Programa encerrado.')
        break
    soma += num
    qtd += 1

media = soma/qtd
print(f'A média dos valores digitados é: {media}')
