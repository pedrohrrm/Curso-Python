list_numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = lambda x: x ** 2

list_resultados = []
for i in list_numeros:
    list_resultados.append(quadrado(i))

print(f'Os quadrados dos números{list_numeros} são {list_resultados}')
