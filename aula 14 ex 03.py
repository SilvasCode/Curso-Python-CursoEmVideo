from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[35mSou seu computador... Sera que consegue me vencer?\033[m ')
sleep(2.0)
print('\033[35mAcabei de pensar em um número entre 1 e 10!\033[m')
sleep(1.5)
print('\033[36mSerá que voçe consegue advinhar qual foi?\033[m')
sleep(0.7)
palpite = int(input('Qual é o seu palpite: ').strip())
tentativa = 0
while palpite != computador:
    palpite = int(input('\033[31mErrou! tente mais uma vez: \033[m'))
    tentativa = tentativa + 1
    if palpite < computador:
        print('\033[33mDica: digite um número maior que o último digitado... Tente outra vez!\033[m ')
    elif palpite > computador:
        print('\033[33mDica: digite um número menor que o último digitado... Tente outra vez!\033[m ')
print('\033[32mVoçe acertou com \033[33m{}\033[m \033[32mtentativa(s), Parabéns!\033[m'.format(tentativa))


