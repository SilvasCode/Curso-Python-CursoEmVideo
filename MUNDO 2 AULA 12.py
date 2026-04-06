nome = str(input('Qual é o seu nome: '))
if nome == 'Andrey':
    print('Que nome bonito')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Marcos':
    print('Seu nome é bem popular no brasil')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))