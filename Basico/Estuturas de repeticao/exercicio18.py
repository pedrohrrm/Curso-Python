'''
Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e 
máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, 
e falso, caso contrário.
'''
def validar(frase, min, max):
    entrada = input(frase)
    tam = len(entrada)
    while ((tam < min) or (tam > max)):
        entrada = input(frase)
        tam = len(entrada)
        
    return frase
    

#Programa principal
x = validar('Digite uma fase: ', 10, 50)
print(f'Voce digitou uma frase válida.')

