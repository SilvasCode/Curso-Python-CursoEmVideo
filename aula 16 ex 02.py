tabela = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians',
          'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba',
          'Flamengo', 'Botafogo', 'Gremio', 'EC Vitória', 'Atlético-MG',
          'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')

print('-=-' * 20)
print('TABELA DO CAMPEONATO BRASILEIRO')
print('-=-' * 20)

print('Times:', tabela)
print('-=-' * 20)

print('Os 5 primeiros são:', tabela[:5])
print('-=-' * 20)

print('Os 4 últimos são:', tabela[-4:])
print('-=-' * 20)

print('Times em ordem alfabética:', sorted(tabela))
print('-=-' * 20)

# interação com usuário
time = input('Digite o nome de um time: ').strip()

# normalização (pra evitar erro com maiúsculas/minúsculas)
time_formatado = time.title()

if time_formatado in tabela:
    print(f'O {time_formatado} está na posição {tabela.index(time_formatado) + 1}')
else:
    print('Esse time não está na tabela.')

print('-=-' * 20)
print('Fim')




