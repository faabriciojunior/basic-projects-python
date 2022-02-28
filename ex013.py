salario = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('Qual é a porcentagem de aumento?: '))
salario2 = salario + (salario * aumento /100)
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, aumento, salario2))
