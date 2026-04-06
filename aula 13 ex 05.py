resultado = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        resultado = resultado + num
        cont += 1
print('Voçe informou {} números PARES e soma entre eles é de {}'.format(cont, resultado))