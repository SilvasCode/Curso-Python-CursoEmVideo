id = int(input('Qual é a sua idade: '))
if id < 12:
    print('CRIANÇA ')
elif id >= 12 and id <= 17:
    print('Adolescente ')
elif id >= 18 and id <= 59:
    print('Adulto ')
else:
    print('IDOSO')