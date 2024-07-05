'''
Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maças, 
laranjas ou bananas. Deverá ser apresentado na tela um menu com a opção 1 para maça,
 2 para laranja e 3 para banana. Após escolhida a fruta, deve-se digitar quantas unidades se 
 quer comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostra-lo na tela. 
Considere que uma maça custa 2,30, uma laranja 3,60 e uma banana 1,85.
'''

escolha = int(input('Escolha o que gostaria de comprar: 1- Maçã, 2- Laranja, 3-Banana: '))
quantidade = int(input('Digite a quantidade de frutas que gostaria de comprar: '))

if escolha == 1:
    valor = quantidade * 2.30
    print(f'O total de valor comprando maçãs é: R${valor}')
else:
    if escolha == 2:
        valor = quantidade * 3.60
        print(f'O valor total comprando laranjas é: R${valor}')
    else:
        if escolha == 3:
            valor = quantidade * 1.85
            print(f'O valor total comprando bananas é: R${valor}')
        else:
            print('Produto inexistente.')
