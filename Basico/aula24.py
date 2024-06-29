# Operadores in e not in
# Strings são iteráveis, iteráves é você conseguir navegar item por item.
# 0 1 2 3 4 5 - indice
# P e d r o
# -6-5-4-3-2-1
nome = 'Pedro'
print(nome[2]) #nesse caso quero pegar a letra que está no indice 2 do nome.
print('r' in nome)
print('a' in nome)
print(10 * '-')
print('r' not in nome)
print('a' not in nome)
print(10 * '-')
print(10 * '-')

nome2 = input('Digite seu nome: ')
encontrar = input('Digite a letra que deseja verificar: ')

if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')