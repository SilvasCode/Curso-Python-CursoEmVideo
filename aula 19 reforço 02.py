from time import sleep
aluno = {}

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['nota'] = float(input(f'A média de {aluno["nome"]}: '))

print('=-=' * 10)
print(f'Calculando os dados de {aluno["nome"]}')
sleep(1)

if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado(a)'
elif 5 <= aluno['nota'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado(a)'

print('=-=' * 10)
for k, v in aluno.items():
    print(f' - {k.capitalize()} é igual a: {v}')





