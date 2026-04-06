print('\033[32mVejamos a idade de algumas pessoas\033[m')
print('''
[ 0 ] Homem
[ 1 ] Mulher''')

media_idade = 0
homem_idade = 0
homem_nome = ' '
mulher_nome = ' '
mulher_idade = ' '
mult1 = 0
mult2 = 0

for c in range(0, 4):
    gen = int(input('Qual a Opção? '))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))

    media_idade += idade / 4

    if gen == 0:
        if idade > homem_idade:
            homem_idade = idade
            homem_nome = nome
            mult1 += 1
    elif gen == 1:
        if idade < 20:
            mulher_nome += nome + ', '
            mulher_idade += str(idade) + ', '
            mult2 += 1
    else:
        print('Erro, por favor tente novamente e selecione uma das oções validas')

print(f'A media da idade do grupo é igual a {media_idade} anos')
if mult1 >= 1:
    print(f'O homem mais velho é {homem_nome} com {homem_idade} anos')
if mult2 >= 2:
    print(f'O número de mulheres menores de 20 anos é {mult2}, são elas {mulher_nome} com respectivamente {mulher_idade} anos')