real = float(input('Quanto dinheiro voçe tem na sua carteiras? R$'))
dolar = real/5.43
euro = real/6.35
print('Com R${:.2f} voçe pode comprar U${:.2f}'.format(real, dolar))
print('Com R${:.2f} voçe pode comprar {:.2f} euros'.format(real, euro))

