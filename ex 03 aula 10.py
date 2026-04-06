from time import sleep
número = int(input('Digite qualquer valor: '))
print('ANALISANDO O VALOR...')
sleep(0.8)
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))

