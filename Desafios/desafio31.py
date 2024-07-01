paridade = lambda x: 'Par' if x % 2 == 0 else 'Impar'

user_num = int(input('Digite um número para verificarmos a pardidade dele: '))

print(f'O {user_num} é {paridade(user_num)}')