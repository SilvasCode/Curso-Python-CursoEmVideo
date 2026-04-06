numeros = []
mais = 0
menos = 0
for i in range(5):
    num = int(input(f"Digita o {i+1}º número: "))
    numeros.append(num)
print(f'A tua lista é: {numeros}')
print(f'O maior valor foi: {max(numeros)} nas posições: {[i for i, v in enumerate(numeros) if v == max(numeros)]}')
print(f'O menor valor foi: {min(numeros)} nas posições: {[i for i, v in enumerate(numeros) if v == min(numeros)]}')

