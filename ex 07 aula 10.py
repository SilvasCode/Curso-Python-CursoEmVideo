from time import sleep
salario = float(input('Qual é o salário do funcionário? R$: '))
print('CALCULANDO...')
sleep(0.8)
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('O novo salário do funcionário com um aumento de 15% será de R${:.2f}'.format(novo))
else:
    salario >= 1250
    novo = salario + (salario * 10 / 100)
    print('O novo salário do funcionário com um aumento de 10% será de R${:.2f}'.format(novo))

