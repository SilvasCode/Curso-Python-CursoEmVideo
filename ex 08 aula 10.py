from time import sleep
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('|          ANALISADOR DE TRIANGULO          |')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
r1 = float(input('Primeiro¹ seguimento: '))
r2 = float(input('Segundo² seguimento: '))
r3 = float(input('Terceiro³ seguimento: '))
print('CALCULANDO R1...')
sleep(0.7)
print('CALCULANDO R2...')
sleep(0.8)
print('CALCULANDO R3...')
sleep(0.9)
print('CALCULO GERADO!')
sleep(0.7)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triangulo!')