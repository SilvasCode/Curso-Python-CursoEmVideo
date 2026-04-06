from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
op = soma = vezes = maior = 0
while op != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos Valores 
    [ 5 ] Sair Programa''')
    op = int(input('>>> Qual é a sua opção: '))
    if op == 1:
        soma = v1 + v2
        print('=================================' * 2)
        print('A soma entre {} e {} é igual a: {}'.format(v1, v2, soma))
        print('=================================' * 2)
    elif op == 2:
        vezes = v1 * v2
        print('=================================' * 2)
        print('A multiplicação entre {} e {} é igual a: {}'.format(v1, v2, vezes))
        print('=================================' * 2)
    elif op == 3:
        if v1 > v2:
            print('=================================' * 2)
            print('O valor {} é maior que o valor {}'.format(v1, v2))
        elif v1 < v2:
            print('O valor {} é menor que o valor {}'.format(v1, v2))
        else:
            print('O valor {} e o valor {} são iguais'.format(v1, v2))
            print('=================================' * 2)
    elif op == 4:
        print('=================================' * 2)
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
        print('=================================' * 2)
    elif op > 5:
        print('=================================')
        print('Opção inválida tente novamente ')
        print('=================================')
    else:
        print('Finalizando...')
        sleep(0.9)
        print('=================================')
print('Programa finalizado com sucesso volte sempre!')







