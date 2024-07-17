'''
Escreva um algoritmo que leia dois valores e imprima na tela o resultado da multiplicação de ambos. 
Porém, para calcular a multiplicação, utilize somente operações de soma e subtração.
 Lembrando que uma multiplicação pode ser considerada como um somatório sucessivo. 
 Utilize esta lógica para construir seu algoritmo.
'''

valor1 = int(input('Digite o primeiro valor: '))
multip = int(input('Digite o segundo valor:'))
valor = 0
i = 0
while (i < multip):
    valor = valor + valor1
    i += 1
print(f'A multiplicao entre os dois numeros, calculada com somas sucessivas é de: {valor}')
