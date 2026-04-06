while True:
    nome = input("Digite seu nome: ")
    if nome.isalpha():
        print(f"Olá, {nome.capitalize()}!")
        break
    else:
        print("Erro: O nome deve conter apenas letras.")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        print(f"Sua idade é {idade}.")
        break # Sai do loop se a conversão der certo
    except ValueError:
        print("Erro: Por favor, digite apenas números (sem letras ou símbolos).")
if idade >= 18:
    print(f'Ola, {nome}! voçe é maior de idade.')
else:
    print(f'Olá, {nome}! voçe é menor de idade.')


