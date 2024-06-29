"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal #é aconselhado o uso quando realmentte faz diferença os últimos números após as casas decimais.

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')

print(round(numero_3, 3))
#função round vai receber os números e no segundo argumento voce passa a quantidade de casas decimais.

#usando o import do decimal:

numero_1 = decimal.Decimal('0.1') #temos que passar os valores no formato string.
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)