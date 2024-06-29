"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(lista_enumerada) #Vai exibir um código estranho que é do iterator.

for indice, nome in lista_enumerada:
    # indice, nome = item #desempacotando os itens da tupla., porem podemos fazer no prórpio for.
    print(indice, nome)
#nesse for eu já consumi os itens do iterator, ou seja, na lista não vai existir mais valores para ser exibidos
# pois paro o ponteiro no fim da lista
# Logo o que pode ser feito é tentar converter o enumerate em um tipo de lista.
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)