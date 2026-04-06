cont = maior = 0
num = int(input('Digite um número, ou digite [0] para sair: '))
while num != 0:
    cont += 1
    if num > maior:
        maior = num
    num = int(input('Digite um número, ou digite [0] para sair: '))
print(f'Foram digitados {cont} valores, e o maior valor digitado foi o número {maior} ')
