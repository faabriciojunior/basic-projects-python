print('Vamos calcular as parcelas do produto!')
produto = str(input('Qual é o produto?: '))
vista = float(input('Valor do produto a vista: R$'))
parcela = int(input('Parcelado em quantas vezes?: '))
valorparcela = vista / parcela
print('O valor do(a) {} a vista é R${:.2f}, e parcelado em {}x sem juros, fica R${:.2f}'.format(produto, vista, parcela, valorparcela))
