'''
Escreva uma rotina que crie um laço de repetição que faz uma contagem e imprime esta contagem na tela em uma só linha. 
Porém, como parâmetro, a função deve receber o valor inicial da contagem, o final, e o passo da iteração. 
Deixe os parâmetros inicial e de passo como opcionais. Você pode fazer o laço com for ou com while.
'''
def contagem (x, y, z):
    for i in range(x, y+1, z):
        print(i, ' ', end='')

contagem(10, 20, 1)