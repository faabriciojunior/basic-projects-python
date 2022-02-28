n1 = float(input('Qual é o preço do produto? R$'))
desconto = int(input('Quanto é o desconto?: '))
novo = n1 - (n1 * desconto / 100)
print('O produto que custava {}, na promoção com desconto de %{} vai custar R${:.2f}'.format(n1, desconto, novo))