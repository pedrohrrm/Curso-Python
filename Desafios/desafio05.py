x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

soma = x + y
subtra = x - y

print(f'A soma é: {soma}')
print(f'A subtração é: {subtra}')

teste_a = soma > 10
teste_b = subtra < 0

print(f'A soma é maior que 10? {teste_a}')
print(f'A subtração é menor que 0? {teste_b}')