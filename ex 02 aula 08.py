from math import hypot
cat = float(input('Comprimento do cateto oposto:'))
adj = float(input('Comprimento do cateto adjacente:'))
hipo = hypot(cat, adj)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
