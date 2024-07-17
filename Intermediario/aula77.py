#Exercício - Sistema de Perguntas e respostas

perguntas = [
{
    'Pergunta': 'Quanto é 2+2 ?',
    'Opções': ['1','3','4','5'],
    'Resposta':'4',
},
{
    'Pergunta': 'Quanto é 5*5 ?',
    'Opções': ['25','55','10','50'],
    'Resposta':'25', 
},
{
    'Pergunta': 'Quanto é 10/2 ?',
    'Opções': ['1','3','4','5'],
    'Resposta':'4',
},
]

qts_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
    
    acerto = False
    int_escolha = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        int_escolha = int(escolha)

    if int_escolha is not None:
        if int_escolha >= 0 and int_escolha < qtd_opcoes:
            if opcoes[int_escolha] == pergunta['Resposta']:
                acerto = True
                
    
    if acerto:
        qts_acertos += 1
        print('Acertou 🥳')
    else:
        print('Errou 😭')
    
print('Você acertou', qts_acertos, 'de', len(perguntas), 'perguntas.')