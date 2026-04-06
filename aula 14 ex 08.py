print('-' * 35)
print('SEQUENCIA DE FIBONACCI')
print('-' * 35)
A = 0
B = 1
C = 1
n = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))
while C <= n:
    print(A, end=" ")
    Aux = A + B
    A = B
    B = Aux
    C += 1
print('FIM')


