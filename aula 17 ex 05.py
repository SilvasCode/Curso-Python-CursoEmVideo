números = []
pares = []
impares = []
resp = ''
while True:
    números.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 30)
print(f'A lista completa é {números}')
print(f'A lista de pares é {pares}')
print(f'A lista de Ìmpares é {impares}')

