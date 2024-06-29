"""
Retorno de valores das funções (return)
"""

def soma (x, y):
    #print(x + y) não retorna valor
    if x > 10:
        return 10, 20
    return x + y

soma1 = soma(1, 2)
soma2 = soma(1, 4)
print(soma1 + soma2)

print(soma(11,55))
variavel = print('Pedro')