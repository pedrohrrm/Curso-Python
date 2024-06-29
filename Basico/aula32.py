"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_text = 'Ímpar'
    if par_impar is True:
        par_impar_text = 'Par'
    print(f'O número {entrada_int} é {par_impar_text}')
else:
    print('Não foi digitado um número inteiro. ')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada_hora = input('Digite a hora atual: ')
if entrada_hora.isdigit():
    entrada_hora_int = int(entrada_hora)
    if entrada_hora_int >= 0 and entrada_hora_int <= 11:
        print(f'Bom dia, o horário é:{entrada_hora_int}')
    elif entrada_hora_int >= 12 and entrada_hora_int <= 17:
        print(f'Boa tarde, o horário é: {entrada_hora_int}')
    else:
        print(f'Boa noite,  o horário é: {entrada_hora_int}')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
letras = len(nome)
if letras > 0 and letras <= 4:
    print(f'Seu nome é curto pois tem {letras} letras.')
elif letras >= 5 and letras <= 6:
    print(f'Seu nome é normal, pois tem {letras} letras.')
elif letras > 6:
    print(f'Seu nome é grande, pois tem {letras} letras')
else:
    print('Não foi digitado nenhum nome.')