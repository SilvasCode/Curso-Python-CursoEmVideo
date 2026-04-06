n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a: {:.1f} '.format(n1, n2, media))
if media < 5.0:
    print('Aluno em RECUPERAÇÃO ')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em RECUPERAÇÃO ')
elif media >= 7.0 and media <= 8.9:
    print('Aluno APROVADO ')
else:
    print('Aluno está de PARABENS!')
