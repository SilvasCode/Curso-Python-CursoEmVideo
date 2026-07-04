from interface import menu
from arquivo import (
    arquivoExiste,
    criarArquivo,
    lerArquivo,
    cadastrar
)

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Sair do sistema'
    ])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')