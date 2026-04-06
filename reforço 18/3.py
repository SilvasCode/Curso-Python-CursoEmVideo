#Declaração de variáveis
lista = []
resp = ''
#looping
while True:
    #Entradas
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    #Saída
    if resp == 'N':
        break
#Oque será mostrado no Terminal.
print('=-' * 20)
print(f'Ao total foram digitados: {len(lista)} números.')
print(f'A lista em ordem crescente: {sorted(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 consta na lista.')
else:
    print('O valor 5 não consta na lista.')

