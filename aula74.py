"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!!'
    return saudar


falar_dia = criar_saudacao('Bom dia!')
falar_noite = criar_saudacao('Boa noite!')

for nome in ['Pedro', 'Maria', 'João']:
    print(falar_dia(nome))
    print(falar_noite(nome))