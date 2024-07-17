# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome' : 'Pedro',
    'sobrenome' : 'Henrique1',
    'sobrenome' : 'Henrique2',
    'sobrenome' : 'Henrique3',
    'idade' : 70,
}
# print(len(pessoa)) #retorna a quantidade de chaves que tem no dict

# print(pessoa.keys()) #retorna as chaves, pode ser convertido em tuplas, listas...

print(list(pessoa.items())) #items são as chaves e os valores.

# nesse caso, se vier a idade da lista, usa o da lista, se não usa o padrão que definimos no set default.
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

#cópia rasa: shallow cop

d1 = {
    'c1': 1,
    'c2' :2,
}

d2 = d1
# nesse tipo de cópia, ele aponta para o dicionário, logo se eu fizer alteração no dicionário1(d2), elas
# também vão afetar o d1

# temos tambeḿ a cópia rasa, .copy. porém quando temos valores mútaveis, lista e outros por ex.
# ai fazer isso, vamos está apenas apontando os valores e não fazendo uma cópia.
# ou seja vai só linkar e fazer uma cópia rasa.

d1 = {
    'c1': 1,
    'c2' :2,
    'l1' : [1, 2, 3],
}
d2 = d1.copy()

d2['c1'] = 100000
d2['l1'][1] = 1111

print(d1)
print(d2)

# temos também o deep copy, que seria uma cópia profunda, nesse caso tenho que fazer o import
# da bibi copy
import copy
d2 = copy.deepcopy(d1)

#Temos o comando pop que vai apagar um item com a chave específica. No caso, vai exibir a chave e apagá-la.
# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

#temos o popitem, ele vai apagar o último item adicionado.
# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)

#O comando update vai atualizar o dicionário de acordo com a chave que eu passar. Podemos passar iteráveis, que se comportam como dicionários
#por exemplo listas e outros.
pessoa.update({
    'nome':'novo_valor_atualizado'
})
tupla = ('nome', 'novo_valor_tupla'),
pessoa.update(tupla)
print(pessoa)