'''
Suponhamos que desejamos exibir uma série de números na tela, onde os limites de início e fim dessa sequência 
são determinados pelo usuário que executa o programa. 
Crie um algoritmo que leia os valores de ínício e de fim de novo programa, e imprima na tela o intervalo 
de número pares correspondentes.
'''
start = int(input('Digite o primeiro número do intervalo: '))
end = int(input('Digite o ultimo numero do intervalo: '))
i = start
while (i <= end):
    if i%2 == 0:
        print(i)
    else:
        pass
    i += 1
