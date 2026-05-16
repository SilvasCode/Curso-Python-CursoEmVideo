def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        return f'Com [{idade}] anos: VOTO NEGADO.'

    elif idade >= 18 and idade < 65:
        return f'Com [{idade}] anos: VOTO OBRIGATÓRIO.'

    else:
        return f'Com [{idade}] anos: VOTO OPCIONAL'


print('=-=' * 8)
ano_nasc = int(input('Em que ano voce nasceu? '))
print(voto(ano_nasc))