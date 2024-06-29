def potencia (base, expoente=2):
    return base ** expoente

user_number = int(input('Digite o número que será utilizado para base do calculo:'))
user_exponente = input('Digite o número que será utilizado para expoente do calculo, se vocÊ não digitar nada, o valor usado será 2:')

if user_exponente:
    print(f'O resultado é: {potencia(user_number, int(user_exponente))}')
else:
    print(f'O resultado é: {potencia(user_number)}')