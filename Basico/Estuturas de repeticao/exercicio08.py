# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for.
i = 0
pares = 0
cont = 0
for i in range (1, 101, 1):
    if i % 2==0:
        pares = pares + i
        cont = cont + 1
media = pares/cont
print(f'A média dos números pares de 1 a 100 é: {media}')