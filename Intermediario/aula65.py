"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
def Pedro():
    print('Linha 1')
    print('Linha 2')
    print('Linha 3')
    print('Linha 4')
    print('Linha 5')

Pedro()
Pedro()
Pedro()

def imprimir(a, b, c):
    print(a, b, c)
    

imprimir(1, 2, 3)
imprimir(4, 5, 'c')

def saudacao(nome = 'sem nome'):
    print(f'Olá, {nome}')

saudacao('Pedro')
saudacao()