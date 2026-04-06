matriz = [
    [0, 0, 0], #linha 0
    [0, 0, 0], #linha 1
    [0, 0, 0]  #linha 2
]
for linha in range(0, 3): # linha: 0, 1 e 2
    for coluna in range(0, 3): #coluna: 0, 1 e 2
# Para cada linha 0, 1 e 2, percorra 3 elementos.
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor
#Cada valor lido pelo teclado ocupará uma célula dentro da matriz, exem: linha [0] coluna [0] recebe um valor.
print('=-' * 15)
#Uso de um looping externo e outro looping interno, para exibir a matriz em formato de tabela.
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(matriz[linha][coluna], end='  ')#vai mostrar a linha 0 preenchida com os elementos da coluna: 0,1 e 2 e assim sucessivamente.
    print()# o (end=' ' serve para manter a linha e dar espaço entre os números, print() serve para quebrar de linha.