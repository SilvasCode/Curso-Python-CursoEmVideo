resposta = ''
cont = soma = media = maior = menor = 0
while resposta != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Voçe digitou {cont} números e a media foi {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')








