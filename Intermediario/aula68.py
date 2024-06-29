"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1
y = 2
def escopo():
    global y
    y = 10
    x = 2
    print(x)
    print(y)

escopo()
print(x)
print(y)