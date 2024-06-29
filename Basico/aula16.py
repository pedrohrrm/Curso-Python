#if / elif / else
#se / se nao se / se nao

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Você digitou uma opção inválida.')

print("FORA DOS BLOCOS DE CONDIÇÕES!!!!")