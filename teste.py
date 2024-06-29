x = 0
cont = 0
soma = 0
while True:
    x = int(input('Digite um valor (999 para parar): '))
    if x == 999:
        break
    soma = soma + x
    cont += 1
print(f'A soma dos {cont} valores é {soma}')   
