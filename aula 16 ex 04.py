num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número número: ')))
print(f'Voce digitou os valores: {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi encontrado.')
print(f'Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')





