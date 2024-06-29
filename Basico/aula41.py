# while/else
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i+=1
else: #Só é executado quando o while é todo executado, se tivermos um break dentro do while, o else não será executado.
    print("O else foi executado")
print('Fora do while!!!')