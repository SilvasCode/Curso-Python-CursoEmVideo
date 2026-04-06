matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
somapar = soma = maior = 0
for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite um valor para {linha} e {coluna}: '))
        if num % 2 == 0:
            somapar += num
        matriz[linha][coluna] = num
print('=-' * 18)
for linha in range(3): #linha: 0, 1 e 2
    for coluna in range(3): #coluna:0, 1 e 2
        print(matriz[linha][coluna], end='  ')
    print()
print('=-' * 18)
print(f'A soma dos valores Pares é: {somapar}')
for linha in range(3):
    soma+= matriz[linha][2]
print(f'A soma dos valores da 3° coluna é: {soma}')
maior = max(matriz[1])
print(f'O maior valor da segunda linha é: {maior}')