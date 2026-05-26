from time import sleep

c = (
    '\033[m',         # 0 - Sem cores
    '\033[0;30;41m',  # 1 - Fundo Vermelho
    '\033[0;30;42m',  # 2 - Fundo Verde
    '\033[0;30;43m',  # 3 - Fundo Amarelo
    '\033[0;30;44m',  # 4 - Fundo Azul
    '\033[0;30;45m',  # 5 - Fundo Roxo
    '\033[7;30m'      # 6 - Fundo Branco
)

def titulo(msg, cor=0):
    tam = len(msg) + 4

    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


def ajuda(comando):
    titulo(f"Acessando o manual do comando '{comando}'", 4)

    print(c[6], end='')
    help(comando)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)

    opcao = input('Função ou Biblioteca > ').strip()

    if opcao.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break

    sleep(1)
    ajuda(opcao)