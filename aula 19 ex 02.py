from random import randint
from time import sleep
from operator import itemgetter

#Sorteio dos jogadores
jogo = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou: ({v}) no dado.')
    sleep(0.8)
print('=-=' * 10)

#Exibição do Rank
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.8)
print('=-=' * 10)


