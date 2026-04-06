from time import sleep
print('=' * 20)
print('  \033[34mDESCUBRA SEU IMC\033[m   ')
print('=' * 20)
masa = float(input('Masa (Kg): '))
altura = float(input('Altura (M): '))
imc = masa / (altura ** 2)
print('\033[36mPROCESSANDO RESULTADO...\033[m')
sleep(0.7)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voçe está abaixo do peso, \033[33m(Muito cuidado!)\033[m ')
elif imc >= 18.5 and imc < 25:
    print('\033[32m(Parabéns)\033[m, voçe está no peso ideal! ')
elif imc >= 25 and imc <= 30:
    print('Voçe está em sobrepeso, \033[35m(Atenção!)\033[m ')
elif imc >= 30 and imc <= 40:
    print('Voçe está em Obesidade, \033[33m(Muito cuidado!)\033[m ')
else:
    print('Voçe está em obesidade morbida, \033[31m(Procure ajuda médica urgentimente!)\033[m ')
