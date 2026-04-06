from time import sleep
velo = float(input('Qual é a velocidade atual do carro: '))
print('PROCESSANDO...')
sleep(2)
if velo > 80:
    print('MULTADO! Voçe excedeu o limite de velocidade que é de 80Km/h')
    multa = (velo-80) * 7
    print('Voçe deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
