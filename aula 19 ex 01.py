from time import sleep

aluno = {}

# 1. Entrada de dados direta nas chaves
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input('Média: '))

# 2. Lógica da situação (Guardando o resultado dentro do dicionário)
if aluno['média'] >= 7.0:
    aluno['situação'] = '\033[32mAPROVADO(A)\033[0m'
elif 5.0 <= aluno['média'] < 7.0:
    aluno['situação'] = '\033[33mRECUPERAÇÃO\033[0m'
else:
    aluno['situação'] = '\033[31mREPROVADO(A)\033[0m'

print('CARREGANDO OS DADOS DO ALUNO(A)...')
sleep(0.8)
print('=-=' * 11)

# 3. Exibição inteligente (O k e v que você aprendeu!)
for k, v in aluno.items():
    print(f' - {k} é igual a: {v}')

print('=-=' * 11)




