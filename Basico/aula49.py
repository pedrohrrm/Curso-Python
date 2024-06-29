"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero) 
lista[2] = 300
print(lista)
del lista[2]
print(lista)
# adicionar itens na lista:
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)
lista.pop()#remove o ultimo valor.
print(lista)
ultimo_valor = lista.pop(3)
print(lista, 'Removido: ', ultimo_valor)
"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
    print(nome, type(nome))
lista.append('Pedro')
posicao = range(len(lista))
for indice in posicao:
    print(indice, lista[indice])