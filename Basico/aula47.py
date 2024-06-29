"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

segredo = 'faculdade'
letra_correta = ''
tentativas = 0
while True:
    print(f'Tentativa nº {tentativas}.')
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez.')
        continue
    if letra_digitada in segredo:
        letra_correta += letra_digitada #Toda vez que eu voltar no começo do while a concatenação vai permanecer.
    palavra_completa = ''
    for letra_secreta in segredo:
        if letra_secreta in letra_correta:
            palavra_completa += letra_secreta
        else:
            palavra_completa += '*'
    print('Palavra: ', palavra_completa)
    if palavra_completa == segredo:
        os.system('clear')
        print(f'A palavra é: {segredo}')
        print('Você acertou a palavra.')
        print(f'Você precisou de {tentativas} tentativas para acertar.')
        break