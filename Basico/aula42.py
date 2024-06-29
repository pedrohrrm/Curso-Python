frase = 'O python é uma linguagem de programação'\
'multiparadigma.'\
'Python foi criado por Guido Van Rossum.'

i=0
quantidade_letra = 0
letra_que_mais_aparece = ''

while i < len(frase):
    letra_atual = frase[i]
  
    if letra_atual == ' ':
        i+=1 #colocamos isso para não perder a função de incrementar o i
        continue

    qtd_atual = frase.count(letra_atual)
    
    if quantidade_letra < qtd_atual:
        quantidade_letra = qtd_atual
        letra_que_mais_aparece = letra_atual
       
    i+=1

print('A letra que apareceu mais vezes foi'
      f'"{letra_que_mais_aparece}" que apareceu'
      f'{quantidade_letra}x')