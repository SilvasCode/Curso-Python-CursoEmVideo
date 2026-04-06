print ('-'*10,'BANCO','-'*10)

a = int(input('Quanto você quer sacar? : '))
cinquenta = 0
dez = 0
um = 0
while a - 50 >= 0:
    a -= 50
    cinquenta += 1
while a - 10 >= 0:
    a -= 10
    dez += 1
while a - 1 >= 0:
    a -= 1
    um += 1
print(f'''são:
{cinquenta} cedula(s) de R$50
{dez} cedula(s) de R$10
{um} cedula(s) de R$1''')