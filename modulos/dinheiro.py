def metade(num):
    helf = num / 2
    return f'A metade de R${num:.2f} é R${helf:.2f}'


def dobro(num):
    double= num * 2
    return f'O dobro de R${num:.2f} é R${double:.2f}'


def aumentodez(num):
    new_price = num * 1.10
    return f'Aumento 10% temos: R${new_price:.2f}'
