age = int(input('Qual a sua idade: '))
sex = input('Qual seu gênero? (M/F): ').upper

while(age>0):
    if(sex == 'M'):
        print(f'Olá senhor, sua idade é: {age}')
        break
    if(sex == 'F'):
        print(f'Olá senhora, sua idade é: {age}')
        break
if (age < 0):    
    print(f'A idade digitada é negativa: {age}')

    '''
    CÓDIGO USADO NA RESPOSTA DO PROBLEMA PELO PROF



    idade = int(input('Qual sua idade?'))
while (idade > 0):
  sexo = input('Qual seu sexo? (M ou F). ')
  if ((sexo == 'M') or (sexo == 'm')):
    print(f'Boa noite Senhor, sua idade é {idade}.')
  else:
    if ((sexo == 'F') or (sexo == 'f')):
      print(f'Boa noite Senhora, sua idade é {idade}.')
    else:
      print('Opção de sexo inexistente.')
  idade = int(input('Qual sua idade?'))
print('Encerrando...')
    '''