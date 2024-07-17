'''
Crie um programa que calcule a soma de 5 valores inteiro. 
Cada valor a ser somado é digitado pelo usuário. Imprima a soma na tela. 
Após a soma, calcule também a média dos valores e mostre na tela.
'''
cont = 0

valor = 0

while cont < 5:
    num = int(input('digite o valor para ser calculado a soma e média: '))
    valor = valor + num
    cont += 1
print(f'A soma dos valores é: {valor} e a média é: {valor/5}')