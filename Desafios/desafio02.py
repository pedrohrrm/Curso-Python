dias = int(input('Digite quantos dias: '))
seg_dias = dias * 86400
horas = int(input('DIgite quantas horas: '))
seg_hora = horas * 3600
minutos = int(input('Digite quantos minutos: '))
min_seg = minutos * 60
segundos = int(input('Digite quantos segundos: '))

total = seg_dias + seg_hora + min_seg + segundos
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos, correspondem a {total} segundos')