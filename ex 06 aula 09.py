nome = str(input('Digite seu nome completo: ')).strip()
#ANDREY ALMEIDA DA SILVA
n = nome.split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

