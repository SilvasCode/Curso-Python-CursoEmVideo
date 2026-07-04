def menu(lista):
    print('-' * 40)
    print('MENU PRINCIPAL')
    print('-' * 40)

    for i, item in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[34m{item}\033[m')

    print('-' * 40)
    return int(input('\033[33mSua opção:\033[m '))