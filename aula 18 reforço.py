números = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        números[0].append(num)
    elif num % 2 == 1:
        números[1].append(num)
print('=' * 38)
números[0].sort()
números[1].sort()
print(f'Os valores Pares digitados foram: {números[0]}')
print(f'Os valores Ímpares digitados foram: {números[1]}')


