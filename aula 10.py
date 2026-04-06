n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi: {:.2f}'.format(m))
if m >= 6.0:
    print('Sua nota está na média, PARABENS!')
else:
    print('Sua nota está abaixo da média, ESTUDE MAIS!')
