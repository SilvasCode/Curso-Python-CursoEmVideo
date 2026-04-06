from random import randint
from time import sleep
computador = randint(0, 10)
print('=======================================================')
print('\033[35;40mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('=======================================================')
print('\033[36mPENSANDO...\033[m')
sleep(0.7)
jogador = int(input('Em que número eu pensei?'))
print('\033[36mLOADING...\033[m')
sleep(0.7)
if jogador == computador:
    print('Parabens voçe consegiu me vençer!')
else:
    print('GANHEI! Pensei no número \033[33m{}\033[m e não no número \033[31m{}\033[m'.format(computador, jogador))

