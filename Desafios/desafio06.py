'''Desenvolva um [[algoritmo]] que solicite o seu ano de nascimento e o ano atual. 
Calcule a sua idade e apresente na tela. Para fins de simplificação, despreze o 
dia e o mês do ano. Após o cálculo, verifique se a idade é maior ou igual a 18 anos 
e apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.'''

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - ano_nasc
print(f'Sua idade é {idade} anos')

if (idade >= 18):
    print('Voce já pode tirar habilitação.')
