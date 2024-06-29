"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 #velocidade atual do carro
local_carro = 101 #velocidade que o carro está na estrada

RADAR_1 = 60 #velocidade max do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distância que o radar pega.

# if velocidade > RADAR_1:
#     print('Velocidade acima do permitido.')
#     if local_carro > = (LOCAL_1 + RADAR_RANGE) and \
#         (RADAR_RANGE - LOCAL_1):
#         print('O carro foi multado.')
# else:
#     print('O carro não foi multado e não ultrapassou a velocidade máxima.')

#DEIXANDO O CÒDIGO MENOS COMPLEXO:

vel_carro_passou_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
         (RADAR_RANGE - LOCAL_1)

if vel_carro_passou_radar1:
    print('Velocidade carro passou do radar 1.')
if carro_multado_radar1 and vel_carro_passou_radar1:
    print('Carro multado em radar 1')