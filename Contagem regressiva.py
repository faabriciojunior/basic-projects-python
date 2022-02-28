print('Vamos descobrir em que ano você nasceu!')
idade = int(input('Quantos anos você tem? '))
ano = int(input('Em que ano estamos? '))
idade2 = ano - idade
print('Você nasceu no ano de {}.'.format(idade2))
print('Agora escolha um ano, e vamos descobrir quantos anos você terá!')
ano2 = int(input('Escolha um ano: '))
print('No ano de {} você terá {} anos.'.format(ano2, ano2-idade2))