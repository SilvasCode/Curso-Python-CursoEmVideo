lista = []
resp = ''
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 25)
print(f'Voce digitou {len(lista)} Elementos')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado e não esta na lista')
