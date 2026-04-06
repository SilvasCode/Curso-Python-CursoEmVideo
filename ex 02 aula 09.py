valor = int(input('Digite um número:'))
#Zona de calcúlos:
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
#Confira os resultados abaixo:
print('Analisando o número {}'.format(valor))
print('Valor de unidade é: {}'.format(u))
print('Valor de dezena é: {}'.format(d))
print('Valor de centena é: {}'.format(c))
print('Valor de milhar é: {}'.format(m))
