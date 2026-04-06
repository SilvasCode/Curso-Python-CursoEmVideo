from datetime import date
menores = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - pessoa < 21:
        menores += 1
print('\n{} são Maiores e {} são menores.'.format(7 - menores, menores))
