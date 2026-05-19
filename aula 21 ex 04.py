def leiaInt(msg):
    """
    -> Valida a entrada de dados para aceitar apenas números inteiros.
    :param msg: O texto que será exibido na tela para o usuário.
    :return: Retorna o valor numérico inteiro validado.
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# [--- Programa Principal ---]
n = leiaInt('Digite un número: ')
print(f'Você acabou de digitar o número {n}')