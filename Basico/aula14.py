a = 'A'
b = 'B'
c = 1.1
string = 'a = {}, b = {} e c = {nome3:.2f}'
formato = string.format(
    a, b, nome3 = c) #podemos nomear os parâmetros, porém se nomearmos o 'a', teremos que nomear todos que vem após....


print(formato)