"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Pedro')
nome = lista.pop()#vai remover o ultimo item da lsita.
lista.append(1234)
del lista[-1]
lista.insert(0, 5)#no métdoo insert passamos 2 parametros, o primeiro a posição que vamos inserir e depois o item que vamos inserir.
print(lista)
#podemos usar o lista.clear() para limpar a lista.
lista.insert(10000000, 56) #nesse caso o python vai inserir o item no ultimo lugar da lista, ele não vai levar em consideração o index que passamos para inserir.
print(lista)