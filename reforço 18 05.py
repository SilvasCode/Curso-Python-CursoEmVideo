boletim = []

while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    aluno = [nome, n1, n2]
    boletim.append(aluno)

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print('=-' * 28)
print('No.  Nome      Média')

for i, aluno in enumerate(boletim):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i}    {aluno[0]}      {media:.1f}')

print('=-' * 28)

while True:
    print('-' * 28)
    opcao = int(input('Mostrar notas de qual aluno? (999 para parar): '))

    if opcao == 999:
        break

    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]} são: {boletim[opcao][1:]}')
    else:
        print('Aluno não existe.')

