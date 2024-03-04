p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O produto custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}'.format(p, d))