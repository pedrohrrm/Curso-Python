# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multi (*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multi_1 = multi(1, 2, 3, 4, 5)
print(multi_1)
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def paridade ():
    numero = input('Digite um número: ')
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'{numero_int} é par!')
    else:
        print(f'{numero_int} é ímpar!')
paridade()