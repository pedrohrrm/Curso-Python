def validacao (pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def soma_total(min, max):
    soma = 0
    i = min
    while(i <= max):
        soma += i
        i += 1
    return soma


x = validacao('Digite um valor inteiro positivo: ', 1, 999)
y = validacao('Digite outro valor inteiro positivo: ', 1, 999)

print(f'O somatório de {x} e {y} é {soma_total(x,y)}')

