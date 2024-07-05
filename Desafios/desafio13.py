x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
escolha = input('Digite a operação que você deseja: +, -, + ou /')

if escolha == '+':
    resultado = x + y
    print(f'O resultado da operação é {resultado}')
elif escolha == '-':
    resultado = x - y
    print(f'O resultado da operação é {resultado}')
elif escolha == '*':
    resultado = x * y 
    print(f'O resultado da operação é {resultado}')
elif escolha == '/':
    resultado = x / y
    print(f'O resultado da operação é {resultado}')
else:
    print('Operação inválida!')