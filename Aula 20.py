def linha():
    """Função simples para desenhar uma linha separadora."""
    print('-' * 30)


def titulo(msg):
    """Função com parâmetro para criar cabeçalhos centralizados."""
    linha()
    print(msg.center(30))
    linha()


def contador(*num):
    """Função com empacotamento para contar e somar números recebidos."""
    tam = len(num)
    soma = sum(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números.')
    print(f'A soma de todos os valores é: {soma}')


# --- PROGRAMA PRINCIPAL ---
titulo('CURSO EM VÍDEO')
titulo('AULA 20 - FUNÇÕES')

# Usando a função com parâmetros fixos
print('Calculando áreas:')
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

area(5, 10)
area(larg=8, comp=2) # Passagem nominal

linha()

# Usando empacotamento (vários números)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)