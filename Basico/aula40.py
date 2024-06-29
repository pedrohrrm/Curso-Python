#calculadora com while

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite um operador (+-/*): ')
    numeros_validos = None #vamos atrelar uma flag nessa variável.
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True #se chegar nessa linha os números são válidos.
    except Exception:
        numeros_validos = None

    if numeros_validos is None:
        print('Os números digitados são inválidos!')
        continue #se os números forem invalidos, o continue vai retornar o código para o ínicio, evitando erro nos calculos.

    operadores_permitidos = '*-/+'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador por vez.')
        continue

    if operador == '+':
        resultado_soma = num_1_float + num_2_float
        print(f'A soma é: {num_1_float} + {num_2_float} = {resultado_soma}')
    elif operador == '-':
        resultado_subtracao = num_1_float - num_2_float
        print(f'A subtração é: {num_1_float} - {num_2_float} = {resultado_subtracao}')
    elif operador == '/':
        resultado_divisao = num_1_float/num_2_float
        print(f'A divisão é: {num_1_float} / {num_2_float} = {resultado_divisao}')
    elif operador == '*':
        resultado_multiplicacao = num_1_float*num_2_float
        print(f'A multiplicação é: {num_1_float} * {num_2_float} = {resultado_multiplicacao}')
    else:
        print('Algo deu errado!')
        continue
    sair = input('Você deseja sair? [s]im ou [n]ão: ').lower().startswith('s') #métodos para converter tudo em minúsculas e identificar a letra que a palavra começa.
    if sair is True:
        break