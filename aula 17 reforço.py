valores = []
pares = []
impares = []
resp = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 30)
print(f'Voce digitou: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores ímpares: {impares}')

