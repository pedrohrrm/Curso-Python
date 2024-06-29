"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Pedro', 'João', 'Maria'] 
nome1, nome2, nome3 = nomes
print(nome1)
#podemos fazer assim também:
nome1, *resto = ['Pedro', 'João', 'Maria'] #por convenção, usamos '*_' para representar o resto, e não a palavra resto, aqui usamos só por exemplicar
print(nome1, resto)
#com a convenção vai ficar:
_, nome1, *_ = ['Pedro', 'João', 'Maria'] #por convenção, usamos '*_' para representar o resto, e não a palavra resto, aqui usamos só por exemplicar
print(nome1, _)
