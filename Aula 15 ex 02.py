cont = 1
resultado = 0
while True:
    print('=' * 58)
    num = int(input('Quer ver a tabuada de qual valor [negativo para finalizar]: '))
    if num <0:
        break
    for cont in range (0, 10 ):
        cont += 1
        resultado = num * cont
        print(f'{num} x {cont} = {resultado}')
print('Programa de tabuada encerrado. Volte sempre.')
print('Fim')