lista_principal = [[], []]
for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista_principal[0].append(num)
    elif num % 2 == 1:
        lista_principal[1].append(num)
print('=' * 30)
lista_principal[0].sort()
print(f'Os valores Pares digitados foram: {lista_principal[0]}')
lista_principal[1].sort()
print(f'Os valores ímpares digitados foram: {lista_principal[1]}')


