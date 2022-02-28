dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diasvalor = dias * 60
kmvalor = km * 0.15
total = diasvalor + kmvalor
print('O total a pagar é de R${:.2f}'.format(total))