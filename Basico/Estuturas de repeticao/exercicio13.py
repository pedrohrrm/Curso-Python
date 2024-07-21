'''Escreva um algoritmo que obtenha do usuário uma frase de tamanho entre 10 e 30 caracteres (faça a validação deste dado). 
Após a frase ter sido digitada corretamente, faça a impressão dela na tela da maneira exata como foi digitada e, em seguida, 
remova os espaços da frase e imprima novamente, sem espaços.'''

frase = input('Digite uma frase: ')
tamanho_frase = len(frase)
while((tamanho_frase < 10) or (tamanho_frase > 30)):
    frase = input('Digite uma frase: ')
    tamanho_frase = len(frase)
print(f'Com espaços: {frase}')
print('Sem espaços: ', end='')
for i in range(0, tamanho_frase):
    if frase[i] != ' ':
        print(frase[i], end='')