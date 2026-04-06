import math
print('================================================')
angulo = float(input('Digite o angulo que voçe deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O angulo de {:.2f} tem o COSENO DE {:.2F}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
