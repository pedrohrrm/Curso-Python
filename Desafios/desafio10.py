'''Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa. 
Ainda, funcionários com mais de 10 anos de empresa tem direito a uma bonificação de 30%. Todos 
os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente. 
Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, 
e apresente a bonificação de cada funcionário na tela.
'''
tempo_servico = int(input('Escreva o tempo de empresa: '))
salario = float(input('Digite o seu salário em R$: '))
if (tempo_servico >= 10 ):
        bonus = salario * 0.3
        print(f'O seu bonus é de 30%, logo seu bonus sera de R${bonus} e o seu salário final será: R${bonus + salario}')
else:
    if (tempo_servico > 5):
        bonus = salario * 0.2
        print(f'O seu bonus é de 20%, logo seu bonus sera de R${bonus} e o seu salário final será: R${bonus + salario}')
    else:
        bonus = salario * 0.1
        print(f'O seu bonus é de 10%, logo seu bonus sera de R${bonus} e o seu salário final será: R${bonus + salario}')