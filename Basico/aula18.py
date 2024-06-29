#if / elif / else
#se / se nao se / se nao
#Não posso ter elif ou else sem um if...

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condicao 1')
elif condicao2:
    print('Código para a condicao 2')
elif condicao3:
    print('Código para a condicao 3')
elif condicao4:
    print('Código para a condicao 4')
else:
    print('Nenhuma condição foi satisfeita.')
#Aqui começa o bloco de código para outro if, que independe do anterior.
if 10 == 10:
    print('Outro IF.')
#Aqui está fora dos blocos do IF.
print('Fora do IF')