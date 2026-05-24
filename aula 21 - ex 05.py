def notas(*num, sit=False):
    ficha = dict()
    ficha['total'] = len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    ficha['media'] = round(sum(num) / len(num), 2)
    print('-=' * 38)

    if sit:
        if ficha['media'] >= 7:
            ficha['situação'] = 'BOA'
        elif ficha['media'] >= 5:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'
    return ficha


#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)


