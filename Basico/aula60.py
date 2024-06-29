"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
basicamente um if else em uma linha
"""
condicao = 10 == 12
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 10
# novo_digito = digito if digito <= 9 else 0
print(digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print('Valor' if True else 'Outro valor' if True else 'Fim')