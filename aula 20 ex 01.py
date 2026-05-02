def calcula_area(larg, comp):
    area = larg * comp
    print(f'O terreno de ({larg:.1f}) x ({comp:.1f}) tem: {area:.1f}m².')


print('-' * 30)
print('Controle De Terreno'.center(30))
print('-' * 30)

while True:
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    calcula_area(larg, comp)
    print('-' * 30)
    while True:
        resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro! Digite apenas S ou N.')
        else:
            break
    if resp == 'N':
        break
    print('-' * 30)

print()
print('Fim Do Programa'.center(30))


