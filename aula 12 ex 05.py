n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {} e {} a média do aluno é {:.2f}'.format(n1, n2, média))
if média > 7:
    print('Aluno APROVADO!')
elif média >= 5 and média < 7:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')