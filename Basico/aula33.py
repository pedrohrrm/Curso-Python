# tipos imutaveis do python: str, int, float, bool
# mais pra frente veremos tipos mutáveis.

string = 'pedro Henrique'
outra_str = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' nesse caso vai dar errado, pois str é imutável
print(string)
print(outra_str)
print(string.capitalize())

print(string.zfill(25))