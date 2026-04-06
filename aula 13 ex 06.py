print('=' * 33)
print('      10 TERMOS DE UMA PA  ')
print('=' * 33)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
decimo = pt + (10 - 1) * rz
for c in range(pt, decimo + rz, rz):
    print(c, ' - ', end=' ')
print('ACABOU')