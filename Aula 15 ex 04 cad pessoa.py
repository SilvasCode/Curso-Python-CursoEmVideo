maior = homens = mvinte = 0
while True:
    print('-' * 20 )
    print('  CADASTRE PESSOAS  ')
    print('-' * 20 )
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mvinte += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homen(s) cadastrados.')
print(f'E temos {mvinte} mulher(s) com menos de 20 anos.')


