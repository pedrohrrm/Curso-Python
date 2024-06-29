# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Pedro Henrique',
    'sobrenome' : 'Ribeiro',
    'idade' : 34,
    'altura' : 1.6,
    'endereco': [
        {'rua': 'xxxx', 'numero': 000},
        {'rua':'aaaaa', 'numero': 111 },
    ],
}
print(pessoa, type(pessoa))
print(pessoa['nome'])

#MANIPULANDO AS CHAVES DO DICIONARIO

pessoa = {

}

# uma parte aleatória do dicionários, podemos adicionar um item e depois procura-lo no dicionário.

pessoa['nome'] = 'PH'
chave = 'nome'

pessoa[chave] = 'Algum nome'
pessoa['sobrenome'] ='Algum sobrenome'

print(pessoa[chave])
pessoa[chave] = 'Maria'

print(pessoa)
print(pessoa['nome'])

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])