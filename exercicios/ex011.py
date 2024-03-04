l = float(input('Largura da parade: '))
a = float(input('Altura da parade: '))
ar = l * a
print('Sua parede tem a dimensão {}x{} e sua área é de {}m2'.format(l, a, ar))
t = ar / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))