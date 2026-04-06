from time import sleep
opção = 0
soma = 0
vezes = 0
maior = 0
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

while opção != 5:
    print('''SELECIONE A OPÇÃO
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>> Qual é a sua opção: '))
    print('=' * 36)
    if opção == 1:
        soma = v1 + v2
        print('A some entre {} e {} é igual: {}'.format(v1, v2, soma))
        print('=' * 36)

    elif opção == 2:
        vezes = v1 * v2
        print('A multiplicação entre {} x {} é igual: {}'.format(v1, v2, vezes))
        print('=' * 36)

    elif opção == 3:
        if v1 > v2:
            print('O valor {} é maior que {}'.format(v1, v2))
        elif v1 < v2:
            print('O valor {} é menor que {}'.format(v1, v2))
        elif v1 == v2:
            print('O valor {} e {} são iguais'.format(v1, v2))
            print('=' * 36)

    elif opção == 4:
        print('Quais são os números novamente? ')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
        print('=' * 36)

    elif opção > 5:
       print('Opção inválida. Tente novamente!')
       print('=' * 36)

    elif opção == 5:
        print('Finalizando...')
        sleep(0.8)
        print('=' * 36)
print('Programa finalizado com sucesso, volte sempre!')

