produto = {}

# 1. Lendo os dados
produto['nome'] = str(input('Nome do produto: ')).strip().capitalize()
produto['preço'] = float(input('Preço: R$ '))
produto['estoque'] = int(input('Quantidade em estoque: '))

# 2. Fazendo o cálculo e criando uma nova chave
# Aqui você pega os valores que já estão no dicionário para calcular o total
produto['total'] = produto['preço'] * produto['estoque']

print('--- RELATÓRIO DO PRODUTO ---')

# 3. Exibindo de forma organizada
for k, v in produto.items():
    # Se a chave for 'preço' ou 'total', formatamos como dinheiro
    if k == 'preço' or k == 'total':
        print(f' - {k.capitalize()}: R$ {v:.2f}')
    else:
        print(f' - {k.capitalize()}: {v}')


