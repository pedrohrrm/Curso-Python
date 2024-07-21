'''
Fatorial é um número inteiro positivo, representado por n!
Calculamos a fatorial pela multiplicação desse número n por todos os seus antecessores até chegar em 1. 
Ainda, fatorial de 0! Sempre será 1.
Considerando a breve explicação sobre fatorial, escreva uma função que calcule o fatorial de um numero 
recebido como parâmetro e retorne o seu resultado. Faça uma validação dos dados através de uma outra função, 
permitindo que somente valores positivos sejam aceitos.
'''

def validar(pergunta):
    x = int(input(pergunta))
    while x < 0:
        x = int(input(pergunta))
    return x

def fatoria(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat = fat * i
    return fat

x = validar('Digite um número para calcular o fatorial: ')
print(f'{x}! é igual a: {fatoria(x)}')


