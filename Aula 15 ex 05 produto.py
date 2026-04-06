preço = total = mil = barato = nbarato = caro = ncaro = 0
produto = saída = ' '
print('-' * 30)
print('      LOJA SUPER PREÇO      ')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço R$: '))
    # Produto acima de mil reais
    if preço >= 1000:
        mil += 1
    # Cálculo dos produtos:
    total = total + preço
    # Produto mais barato
    if barato == 0 or preço < barato:
        nbarato = produto
        barato = preço
    # Produto mais caro
    if caro == 0 or preço > caro:
        ncaro = produto
        caro = preço
    saída = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if saída == 'N':
        break
print('----------{FIM DO PROGRAMA}----------')
print(f'O total da compra foi de R${total:.2f}')
print(f'temos {mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custa R${barato}')
print(f'O produto mais caro foi {ncaro} que custa R${caro}')







