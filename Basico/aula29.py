# Intrudução ao try/except
# try -> tentar executar o código.
# except -> ocorreu algum erro ao tentar executar.

# print(1234)
# print(34563)
# int('a')

numero_str = input('Vou dobrar o número que você digitar: ')
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número.')
