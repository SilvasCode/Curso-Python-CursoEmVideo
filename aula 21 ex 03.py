def jogador(nome_jogador='<Desconhecido>', num_gols=0):
    """
    -> Faz a ficha de um jogador de futebol e mostra seus gols.
    :param nome_jogador: (opcional) O nome do jogador de futebol.
    :param num_gols: (opcional) A quantidade de gols que ele marcou.
    :return: Retorna uma string formatada com a ficha do jogador.
    """
    return f'O jogador [{nome_jogador}] fez [{num_gols}] gol(s) no campeonato.'


# [--- Programa Principal ---]
nome_jogador = str(input('Nome do jogador: ')).capitalize().strip()
num_gols = input('Número de Gols: ')
print('-' * 30)

if nome_jogador == '' and num_gols == '':
    print(jogador())

elif num_gols == '':
    print(jogador(nome_jogador))

elif nome_jogador == '':
    print(jogador(num_gols=int(num_gols)))

else:
    print(jogador(nome_jogador, num_gols))