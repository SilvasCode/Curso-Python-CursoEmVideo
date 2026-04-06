print('{:=^40}'.format(' LOJAS SILVA '))
valor = float(input('Digite o preço do produto R$: '))
print('Escolha a forma de pagamento: \n[1]- À vista no dinheiro ou cheque: 10% de desconto\n[2]- À vista no cartão: 5% de '
      'desconto\n[3]- Em até 2x no cartão: preço normal\n[4]- 3x ou mais no cartão: 20% de juros')
esc = int(input('Digite a forma escolhida: '))
if esc == 1:
    print(f'O valor a se pagar é de R${valor * 0.9:.2f}')
elif esc == 2:
    print(f'O valor a se pagar é de R${valor * 0.95:.2f}')
elif esc == 3:
    print(f'O valor a se pagar é de R${valor:.2f} em duas parcelas de {(valor / 2):.2f}')
elif esc == 4:
    parc = int(input('Quantas parcelas deseja dividir? '))
    print(f'O valor a se pagar é de R${valor * 1.2:.2f} dividido em {parc} parcelas de R${(valor * 1.2) / parc:.2f}')

