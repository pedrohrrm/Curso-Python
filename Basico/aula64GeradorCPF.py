import random
import sys

nove_digit = ''

for i in range(9):
    nove_digit += str(random.randint(0, 9))
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
print(cpf_gerado_pelo_algoritmo)
# if cpf_gerado_pelo_algoritmo == cpf_usuario:
#     print(f'O CPF enviado pelo usuário é válido. CPF: {cpf_usuario}')
# else:
#     print(f'O CPF enviado é inválido, por favor confira e envie de novo.')
