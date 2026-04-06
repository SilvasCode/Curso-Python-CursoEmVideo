from datetime import date
from time import sleep
nasc = int(input('Ano de nascimento: '))
hoje = date.today()
idade = hoje.year - nasc
print('-=' * 10)
print('\033[32mGERANDO RESULTADO...\033[m')
sleep(0.8)
print('O atleta tem \033[34m{}\033[m anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA: \033[36mMIRIM\033[m ')
elif idade <= 14:
    print('CATERGORIA: \033[36mINFANTIL\033[m')
elif idade <= 19:
    print('CATEGORIA: \033[36mJUNIOR\033[m')
elif idade <= 25:
    print('CATEGORIA: \033[36mSENIOR\033[m')
else:
    print('CATEGORIA: \033[36mMASTER\033[m')

