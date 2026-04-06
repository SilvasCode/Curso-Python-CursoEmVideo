from time import sleep
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[36mCALCULANDO...\033[m')
sleep(0.7)
#Estrutura alinhada
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo! ', end='')
    if r1 == r2 == r3:
        print('\033[35mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[35mESCALENO\033[m')
    else:
        print('\033[35mISÓSCELES\033[M')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo')
