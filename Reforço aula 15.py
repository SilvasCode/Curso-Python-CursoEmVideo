cont = idade = soma = media = maioridadehomem = mvinte = 0
nome = sexo = nomevelho = ' '
for p in range(1, 5):
    print(f'----- {p}º Pessoa -----')
    Nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma += idade
    media = soma / cont
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade <= 20:
        mvinte += 1
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {hvelho} e se chama: {nome}')
print(f'Ao todo são {mvinte} Mulher(s) com menos de 20 anos.')





















