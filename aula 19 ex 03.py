from datetime import datetime

# Pegamos o ano atual do sistema
ano_atual = datetime.now().year
dados = {}

# 1. Cadastro Básico
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = ano_atual - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# 2. Bloco Condicional (Só entra se tiver CTPS)
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))

    # Lógica da Aposentadoria:
    # Idade de contratação (contratação - nascimento) + 35 anos de contribuição
    idade_contratacao = dados['contratação'] - nascimento
    dados['aposentadoria'] = idade_contratacao + 35

# 3. Exibição Final (O FOR varre tudo o que estiver no dicionário)
print('=-=' * 10)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


