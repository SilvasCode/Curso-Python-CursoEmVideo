from random import choice
n1 = str(input('Qual é o seu nome:'))
n2 = str(input('Qual é o seu nome:'))
n3 = str(input('Qual é o seu nome:'))
n4 = str(input('Qual é o seu nome:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
