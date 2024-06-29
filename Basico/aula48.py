"""string é uma cadeia de caracteres
Listas em python, tipo list é mutável ou seja é pode ser alterada
suporta valores de vários tipos
"""
string = 'ABCDE' #5 caracteres (len)
lista = [123, True, 'Pedro Henrique', 1.69, []] #podemos inclusive colocar uma lista dentro de outra lista.
#na lista acima é possível acessar os itens um por um, eles também vao ter indices, no caso temos:
print(lista[2]) #nesse ex, vai imprimir o item 2 da lista.
# print(bool([])) #uma lista vazia é false
#alterar o valor da lista:
lista[2] = 'PEdro'#também podemos usar indices negativos.. lista[-3]
print(lista[2])
# print(lista, type(lista))
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #aqui vamos fazer a concatenação das listas. Nesse caso a união das listas
print(lista_c)
lista_d = lista_a.extend(lista_b) #nesse caso vai retornar "None", pois extend não retorna valor.
lista_a.extend(lista_b)
print(lista_a) #vai extender a lista b na lista a, ou seja uma concatenaão porém na lista a.
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_1 = ['Pedro', 'João']
lista_2 = lista_1 #Isso não é cópia, estou fazendo as duas listas apontarem para o mesmo endereço na memŕia.
lista_3 = lista_1.copy() #aqui realizamos uma cópia dos itens da lista_1
lista_1.append(40)
print(lista_2)
print(lista_3)