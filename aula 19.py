user1 = {'nome': 'Andrey', 'idade': 23} #Dicionario é representada por {} ou dict.
user2 = {'nome': 'Ana', 'idade': 20}
lista = []
lista.append(user1) #Pode misturar dicionario com lista. (exem: print(lista[0]): mostra {'nome': 'Andrey', 'idade': 23})
lista.append(user2) #Ou se der um print(lista[0]['nome']) será exibido: 'Andrey'
print(lista[0]['nome'])
