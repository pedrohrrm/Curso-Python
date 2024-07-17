'''
Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final. Para este intervalo especificado pelo usuário, 
calcule e mostre na tela:

1. A quantidade de números inteiros e positivos;
2. A quantidade de números pares;
3. A quantidade de números impares;
4. A respectiva média de cada um dos itens anteriores;

Será necessário criar uma variável distinta para cada somatório, para cada quantidade e para cada média solicitada.'''

inicial = int(input('Qual o valor inicial da contagem: '))
final = int(input('Qual o valor final da contagem: '))

i = inicial
if (inicial < final):
    inteiro = 0
    pares = 0
    impares = 0
    media_inteiros = 0
    media_pares = 0
    media_impares = 0
    while (i <= final):
        if i > 0:
            inteiro +=1
            media_inteiros = i + media_inteiros
        if i % 2 == 0:
            pares = pares + 1
            media_pares = i + media_pares
        if i % 2 != 0:
            impares += 1
            media_impares = i + media_impares
        i += 1
else:
    print('Voce digitou um valor final menor que o inicial')

print(f'A quantidade de números inteiros e positivos é: {inteiro}')
print(f'A media dos valores inteiros e positivos é: {media_inteiros/inteiro}')
print(f'A quantidade de números pares é: {pares}')
print(f'A media dos valores pares é: {media_pares/pares}')
print(f'A quantidade de números impares é: {impares}')
print(f'A média dos valores impares é: {media_impares/impares}')
