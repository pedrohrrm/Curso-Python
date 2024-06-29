"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []
while True:
    print('Selecione uma opção: ')
    print('[1] Para inserir')
    print('[2] Para apagar')
    print('[3] Para listar')
    opcao = input('Escolha: ')
    if opcao == '1':
        os.system('clear')
        insert = input('Digite o que deseja inserir na lista: ')
        lista.append(insert)
        print(f'O item {insert} foi inserido com sucesso.')
        print(lista)
    elif opcao == '2':
        os.system('clear')
        print(lista)
        indice = input('Digite o indice do produto que deseja apagar: ')
        try:
            int_indice = int(indice)
            del lista[int_indice]
            print(f'O item foi removido com sucesso. ')
        except ValueError:
            print('Digite apenas números inteiros.')
        except IndexError:
            print('Por favor, digite apenas itens dentro da lista.')
    elif opcao == '3':
        os.system('clear')
        if len(lista) == 0:
            print('Nada para lista!')

        for i, valor in enumerate(lista):
            print(i, valor)
        
    else:
        os.system('clear')
        print('Opção inválida.')
        continue
