larg = float(input('Qual é a largura da parede:'))
alt = float(input('Qual é a altura da perede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg,alt,área))
tinta = área / 2
print('Para pintar essa parede vai precisar de {}L de tinta'.format(tinta))

