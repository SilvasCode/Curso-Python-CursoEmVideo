nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Quantas letras tem seu nome {}'.format(len(nome.replace(" ", ""))))
print(f"Primeiro nome: {nome.split()[0]}, Letras: {len(nome.split()[0])}")

