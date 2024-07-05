x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

soma = x + y
subtra = x - y

print(f'A soma é: {soma}')
print(f'A subtração é: {subtra}')
if (soma > 10):
    print(f'A soma é maior que 10.')
if (subtra < 0):
    print('A subtração é menor que 0.')