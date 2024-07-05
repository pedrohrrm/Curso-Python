'''
Uma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir. Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. Ao final, apresente o valor total da compra e o valor das parcelas:
Pagamento à vista – conceder desconto de 5%;
Pagamento em 3x – o valor não sofre alterações;
Pagamento em 5x – acréscimo de 2%;
Pagamento em 10x – acréscimo 8%;
'''

valor = float(input('Digite o valor da compra: '))
print('Escolha a opção de acordo com o tipo do pagamento:')
print('1- A vista')
print('2 - 3x cartão')
print('3 - 5x cartão')
print('4 - 10x cartão')
tipo_pagto = int(input())

if tipo_pagto == 1:
    desconto = valor * 5/100
    print(f'O valor final com o desconto de 5% é: R${valor - desconto}')
elif tipo_pagto == 2:
    print(f'Na divisão do valor em 3 parcelas não há desconto no valor, logo o valor final é: R$ {valor}')
elif tipo_pagto == 3:
    acrescimo = valor * 2/100
    print(f'O valor final com o acréscimo de divisão em 5 parcelas é de 2% no cartão: R${valor + acrescimo}')
elif tipo_pagto == 4:
    acrescimo = valor * 8/100
    print(f'O valor final com o acréscimo de divisão em 10 parcelas é de 8% no cartão: R${valor + acrescimo}')
else:
    print('Escolha inválida!')