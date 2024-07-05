valor = float(input('Digite um número'))
if ((-100 < valor) and (valor < -1)) or ((1 < valor) and (valor < 100)):
    print('O valor está contido no intervalo.')
else:
    print('O valor não está contido no intervalo.')