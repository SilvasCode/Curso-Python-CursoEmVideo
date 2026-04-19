dados = dict()

# Coleta de dados básicos
dados['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
numpartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

print('=-=' * 12)
gols = []
soma_gols = 0

# Laço para leitura dos gols e soma do total
for c in range(0, numpartidas):
   numgol = int(input(f' Quantos gols na partida {c+1}: '))
   gols.append(numgol)
   soma_gols += numgol

# Alimentando o dicionário (Fora do laço para maior eficiência)
dados['Gols'] = gols[:]
dados['Total'] = soma_gols

print('=-=' * 12)

# Exibição 1: Dicionário em formato bruto (Debug)
print(dados)

print('=-=' * 12)

# Exibição 2: Estrutura de campos e valores usando .items()
for k, v in dados.items():
    print(f' => O campo {k} tem o valor: ({v})')
print('=-=' * 12)

# Exibição 3: Relatório detalhado do aproveitamento
print(f' O jogador {dados["Nome"]} jogou: {numpartidas} partidas')
for c in range(0, numpartidas):
    # Acessando a lista de gols que está dentro do dicionário
    print(f' => Na partida N°{c+1}, fez ({dados["Gols"][c]}) gols')
print(f'Foi um total de {dados["Total"]} gols')
print('=-=' * 12)