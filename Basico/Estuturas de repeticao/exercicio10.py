# Escreva um algoritmo que calcule e exiba a tabuada de um número escolhido e digitado pelo usuário. 
# A tabuada deve ser calculada até um determinado número n,também fornecido pelo usuário. Implemente o laço usando for.

num = int(input('Digite um número para ser calculado a tabuada: '))
i = 0
for i in range (0, 11):
    print(f'{num}X{i} = {i*num}')