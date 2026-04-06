distancia = float(input('Qual é a distancia da sua viagem: '))
print('Voçe está preste a começar uma viagem de {:.2f}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.40
print('O preço de sua passagem será de R${:.2f}'.format(preço))
