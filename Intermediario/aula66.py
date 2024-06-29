"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    #definição da função 
    print(f'{x=} y={y}','|','x + y = ', x+y)
print(soma)
print(soma(1, 3))
soma(1,2)
soma(y=2,x=1) #para ficar igual o anterior, temos que nomear os argumentos, aí podemos passa-los em qualquer ordem.