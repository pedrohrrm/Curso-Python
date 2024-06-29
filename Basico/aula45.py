"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = iter('Pedro') #iter entrega o objeto iterador, que sabe iterar os itens da string.

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
# Quando acabar os valores, ele vai gerar um erro do tipo "StopIteration", nesse caso, esse erro vai encerrar a buscas.

# outro modo de usar o next é:

print(next(texto))
print(next(texto))
print(next(texto))#O next chama o proximo valor que estiver disponível neste iter.
print(next(texto))