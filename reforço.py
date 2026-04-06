itens = ('Lapis', 1.75, 'Borracha',  2.00,'Caderno', 15.90,
         'Estejo', 25.90,'Transferidor', 4.90,'Compasso', 9.99,
         'Mochila', 120.00,'Canetas', 22.50,'Livros', 34.90)
print('=' * 40)
print('Listagem de preço')
print('=' * 40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end=' ')
    else:
        print(f'R$:{itens[pos]:>8.2f}')

