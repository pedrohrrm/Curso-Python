# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplica(numero):
#     return numero * 2
# def triplica(numero):
#     return numero * 3
# def quadriplica(numero):
#     return numero * 4
# duplicar = print(duplica(2))
# triplicar = print(triplica(2))
# quadriplicar = print(quadriplica(2))

def defina_mutilpicador(multiplicador):
    def operacao(numero):
        return numero * multiplicador
    return operacao
duplicar = defina_mutilpicador(2)