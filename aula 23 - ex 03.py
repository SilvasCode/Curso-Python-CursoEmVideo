print('-' * 30)
print('MANU PRINCIPAL'.center(30))
print('-' * 30)

print('\033[0;033m1 - \033[m \033[0;034mVer pessoas cadastradas\033[m')
print('\033[0;033m2 - \033[m \033[0;034mCadastrar nova pessoa\033[m')
print('\033[0;033m3 - \033[m \033[0;034mSair do sistema\033[m')
print('-' * 30)

while True:
    op = 0
    try:
        op = int(input('Sua Opção: '))
        if op > 3:
            print('\033[0;031mERRO! Digite uma opção válida.\033[m')
        if op == 1:
            print('-' * 30)
            print('Opção 1'.center(30))
            print('-' * 30)
        elif op == 2:
            print('-' * 30)
            print('Opção 2'.center(30))
            print('-' * 30)
    except ValueError:
        print('\033[0;031mERRO: por favor, digite um número inteiro válido.\033[m')
    if op == 3:
        break
print('-' * 30)
print('Saindo do sistema... Até logo.')
print('-' * 30)

