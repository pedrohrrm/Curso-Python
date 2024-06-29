
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
letras = int(len(nome))
invertido = nome[::-1]
if len(nome) > 0 and len(idade) > 0:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome contem {letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é: {nome[len(nome)-1]}')
else:
    print('Você não digitou o nome ou idade.')