casa = float(input('Valor da casa R$' ))
salario = float(input('Salario do comprador R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO ')
else:
    print('Empréstimo NEGADO! ')