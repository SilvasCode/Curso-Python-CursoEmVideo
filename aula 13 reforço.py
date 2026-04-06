somaidade = 0
idade_mais_velho = 0
nome_mais_velho = ''
mulheres = 0

for c in range(1, 5):
    print('----', c, 'PESSOA', '----')

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    somaidade += idade

    # Homem mais velho
    if sexo.upper() == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    # Mulheres com menos de 20
    if sexo.upper() == 'F' and idade < 20:
        mulheres += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_mais_velho, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
