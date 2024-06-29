# Lista de listas e seus indices:
import os
salas = [
    ['Pedro', 'João',],
    ['Paulo',],
    ['Luiz', 'Lucas', 'Mateus',(0, 10, 20, 30, 40)]
]
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])
os.system('clear')
salas = [
    ['Pedro', 'João',],
    ['Paulo',],
    ['Luiz', 'Lucas', 'Mateus',]
]
for sala in salas: #o primeiro for, vai fazer a busca nas salas
    print(f'A sala é {sala}')
    for aluno in sala: #o segundo for vai realizar as buscas nos itens das salas.
        print(aluno)