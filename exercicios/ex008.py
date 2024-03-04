m = float(input('Digite uma distância em metros: '))

# Conversão para quilômetros, hectômetros, decâmetros, decímetros, centímetros, milímetros
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
dm2 = m * 100

# Exibição dos resultados
print('A medida de {:.2f} metros corresponde a:'.format(m))
print('{:.6f} quilômetros'.format(km))
print('{:.4f} hectômetros'.format(hm))
print('{:.2f} decâmetros'.format(dam))
print('{} metros'.format(m))
print('{:.2f} decímetros'.format(dm))
print('{:.2f} centímetros'.format(cm))
print('{:.2f} milímetros'.format(mm))
print('{:.2f} decímetros quadrados'.format(dm2))