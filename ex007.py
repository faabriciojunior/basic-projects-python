n = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
n3 = (n + n2) / 2
print('A média entre {} e {} é: {}'.format(n, n2, (n+n2)/2))
if(n3 >= 5):
    print('Aprovado!')
else:
    print('Reprovado!')