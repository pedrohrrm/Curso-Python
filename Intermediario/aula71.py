"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    valor_total = 0
    for numero in args:
        valor_total += numero
    return valor_total

soma_1 = soma(1,2,3)
print(soma_1)

soma_2 = soma(2,2,2)
print(soma_2)

print(soma_1 + soma_2)