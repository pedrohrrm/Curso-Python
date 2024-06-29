# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, u = lista #detalhe: p é o rimeiro elemento e u o último elemento.
print(p, u)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string) #desse jeito ele itera todos os elemntos da minha lista e iterar eles.
#na declaração, quando temos listas dentro de listas podemos usar um separador com \n para dar uma quebra de linha
# Ex.: print(*salas, sep='\n')