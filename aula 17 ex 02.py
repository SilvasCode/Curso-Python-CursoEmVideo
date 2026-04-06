valores = []
resp = ''
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=-=' * 20)
print(f'Voce digitou os valores: {sorted(valores)}')

