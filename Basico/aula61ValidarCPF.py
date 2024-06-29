"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import sys


cpf_usuario = input('Digite seu CPF(Apenas números): ')\
    .replace('.', '')\
    .replace('-', '') #replace é para tirar os caracteres indesejados e substituir por outros.
# cpf_usuario = '74682489070'
#Validar para verificar se os números estão repetidos:
entrada_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digit = cpf_usuario[:9] #pegar os 9 primeiros dígitos do cpf, que é o objetivo da nossa conta.
contador_regress_1 = 10
resultado_digito_1 = 0
for digito in nove_digit:
    resultado_digito_1 += int(digito) * contador_regress_1 
    contador_regress_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)

contador_regress_2 = 11
dez_digit = nove_digit + str(digito_1)
resultado_digito_2 = 0
for digito in dez_digit:
    resultado_digito_2 += int(digito) * contador_regress_2
    contador_regress_2 -= 1
# print(resultado_digito_2)
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
# print(digito_2)

cpf_gerado_pelo_algoritmo = f'{nove_digit}{digito_1}{digito_2}'

if cpf_gerado_pelo_algoritmo == cpf_usuario:
    print(f'O CPF enviado pelo usuário é válido. CPF: {cpf_usuario}')
else:
    print(f'O CPF enviado é inválido, por favor confira e envie de novo.')














#ESSA SOLUÇÃO COM A RETIRADA DOS PONTOS NÃO SERA USADA NESSE MOMENTO, POR ISSO COMENTEI O QUE HAVIA INICIADO:
# cpf_usuario = '746.824.890-70'
# remove_digito_cpf = cpf_usuario.split('-')
# print(remove_digito_cpf)
# print(remove_digito_cpf[0])
# cpf_num = remove_digito_cpf[0].split('.')
# print(cpf_num)
# cpf_verificar = ''.join(cpf_num)
# print(cpf_verificar)
# 'cpf_int = int(cpf_verificar)'
# cont = 10
# lista_num_multiplicados = []

# for i in cpf_int:
#     multiplica = cpf_int[i] * cont
#     cont =- 1
#     lista = lista_num_multiplicados.append(multiplica)

# print(lista)    