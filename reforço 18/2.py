lista = []
cont = maior = menor = somapar = soma = 0
while True:
    valores = int(input('Digite um valor, ou [999] para parrar: '))
    if valores != 999:
        lista.append(valores)
    else:
        break
    #zona de testes/condicionais
    cont+= 1
    if len(lista) == 1:
        maior = menor = valores
    else:
        if valores > maior:
            maior = valores
        if valores < menor:
            menor = valores
    if valores % 2 == 0:
        somapar+= 1
    soma += valores
#Oque será exibido no terminal
print('=-' * 25)
lista.sort()
print(f'Os valores digitados foram: {lista}')
print(f'Ao total foram digitados: {cont} números')
print(f'O maior número digitado foi: {maior} e o menor foi: {menor}')
print(f'O total foram digitados {somapar} números Pares')
print(f'A soma de todos os valores da lista é de: {soma}')




