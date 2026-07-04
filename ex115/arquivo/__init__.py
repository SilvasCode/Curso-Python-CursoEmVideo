def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mErro ao criar o arquivo.\033[m')
    else:
        print('\033[31mArquivo criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo.\033[m')
    else:
        print('-' * 40)
        print('PESSOAS CADASTRADAS')
        print('-' * 40)

        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mErro ao abrir o arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mErro ao cadastrar.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()