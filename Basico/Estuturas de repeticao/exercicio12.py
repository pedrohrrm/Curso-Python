'''Escreva um algoritmo que encontre todos os números primos de 2 até 99. Imprima na tela todos eles.'''
print('Primos de 0 a 99: ')
for num in range(2, 100, 1):
    marcador = 0
    for i in range(2, num):
        if (num%i == 0):
            marcador = 1
            break
    if marcador == 0:
        print(num)