

salario = float(input('Digite seu salario em R$: '))
tempo = int(input('Digite seu tempo de serviço em anos: '))
if (tempo > 5):
    bonifica = salario * (20/100)
    print(f'Como voce possui {tempo} de serviço na nossa empresa, voce recebeu um bonus de 20%, logo seu novo salário será: R${salario + bonifica}')
else:
    bonifica = salario * (10/100)
    print(f'Como voce possui {tempo} de serviço na nossa empresa, voce recebeu um bonus de 10%, logo seu novo salário será: R${salario + bonifica}')