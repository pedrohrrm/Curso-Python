'''
Escreva uma rotina que crie uma borda ao redor de uma palavra para destaca-la como sendo um título. 
A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de texto deverá ser 
adaptável de acordo com o tamanho da palavra. A seguir veja alguns exemplos de como deve ficar a borda na palavra.

+-------------+
| Vinicius |
+-------------+

+-----+
| Olá |
+-----+
'''


def borda(s):
    print('+','-'*len(s), '+')
    print('|', s, '|')
    print('+','-'*len(s), '+')
borda('Pedro Henrique')
