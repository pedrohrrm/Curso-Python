# Flag (bandeira) - Marcar um local
# None = não Valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade

# id das variáveis na memória
# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print(passou_no_if, passou_no_if is None)#para saber se a var passou_no_if ainda é none, se for true,
# signifca que ainda não entrou no if.
else:
    print('Passou no if')