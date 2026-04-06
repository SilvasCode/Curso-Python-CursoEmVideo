from random import randint
from time import sleep
computador = randint(0, 5)
print('=-'* 25)
print('\033[34mVOU PENSAR EM NÚMERO ENTRE\033[m \033[35m0\033[m \033[34mE\033[m \033[35m5\033[m. \033[34mTENTE ADVINHAR...\033[m')
print('=-'* 25)
jogador = int(input('\033[34mEm que número eu pensei: \033[m'))
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if jogador == computador:
    print('\033[32mParabéns voçe conseguiu me vencer!\033[m')
else:
    print('\033[31mVenci, pensei no número {} e não no número {}!\033[m'.format(computador, jogador))




