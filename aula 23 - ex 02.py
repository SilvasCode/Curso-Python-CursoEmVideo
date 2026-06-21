import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except Exception as erro:
    print(f'O site (Google) não está acessível. Erro: [{erro}]')
else:
    print('Consegui acessar o site com sucesso!')
finally:
    print('Volte sempre!')
