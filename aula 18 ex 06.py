ficha = list()
resp = ''
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    média = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], média])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 28)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 28)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-' * 28)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    if opc <= len(ficha) - 1:
        print(f'Nota de {ficha[opc][0]} são: {ficha[opc][1]}')

