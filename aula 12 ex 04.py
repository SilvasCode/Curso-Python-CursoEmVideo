from datetime import date
atual = date.today().year
sx = str(input('Qual é o seu sexo: '))
nasc = int(input('\033[36mAno de Nascimento: \033[m'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18 and 'Masculino':
    print('Voçe tem que se alistar \033[36mIMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voçe já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Pessoa do sexo FEMININO não pode realizar o alistamento! ')

