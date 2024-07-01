def dobro(num):
    return num * 2
def quadrado(num):
    return dobro(num) ** 2

user_num = int(input('Digite um número para calcularmos o quadrado do seu dobro: '))
print(f'O quadrado do dobro de {user_num} é {quadrado(user_num)}')