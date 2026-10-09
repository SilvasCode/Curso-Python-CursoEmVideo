
try:
    num = int(input('Digite um número: '))
    dob = num * 2
    print(f'Voce digitou o número {num}')
    print(f'O dobro de {num} é {dob}')
except ValueError:
    print('Entrada inválida, Digite apenas números inteiro.')
