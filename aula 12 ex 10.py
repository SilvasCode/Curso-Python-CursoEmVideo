# Pedra papel ou tesoura
from random import randint
from time import sleep
print('-=-'*20)
print('{:^60}'.format('Pedra, Papel ou Tesoura'))
print('-=-'*20)
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
print('-=-'*20)
js = int(input('Qual a sua jogada? '))
pc = randint(1, 3)
lista = ('pedra', 'papel', 'tesoura')
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(1)
print('-=-'*20)
if js == pc:
    print('Empate Computador escolheu {}'.format(lista[pc-1]))
elif js == 1 and pc == 2:
    print('Você Perdeu, Computador escolheu Papel!!!')
elif js == 1 and pc == 3:
    print('Você Ganhou!!!, Computador escolheu Tesoura!!!')
elif js == 2 and pc == 1:
    print('Você Ganhou!!!, Computador escolheu Pedra')
elif js == 2 and pc == 3:
    print('Você Perdeu, Computador escolheu Tesoura')
elif js == 3 and pc == 1:
    print('Você Perdeu, Computador escolheu Pedra')
elif js == 3 and pc == 2:
    print('Você Ganhou!!!, Computador escolheu Papel')
else:
    print('[ERRO] JOGADA INVÁLIDA!')

