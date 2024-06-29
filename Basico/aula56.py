"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só que, frase bacana.'
lista_palavras = frase.split() #se não passar argumentos, ele vai pegar automaticamente com a separação das palavras nos espaço entre elas.
print(lista_palavras)

lista_palavras = frase.split(',')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip()) #strip vai cortar os espaços entre as strings. rstrip corta da direita e lstrip corta da esquerda.
    frase_unida = '-'.join(lista_palavras)
    print(frase_unida)

#Ex do professor:::::
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
