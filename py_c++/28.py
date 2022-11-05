total = mais = menor = i = 0
menorp = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o preco do produto: '))
    total += preco
    if i == 0:
        menor = preco
        menorp = nome
    elif i != 0:
        if preco <= menor:
            menor = preco
            menorp = nome
    cont = ' '
    if preco > 1000:
        mais += 1
    i += 1
    while cont not in 'sn':
        cont = str(input('Deseja continuar? ')).strip().lower()[0]
    if cont == 'n':
        break
print(f'Total gasto e {total}, {mais} produtos custam mais de mil, o produto mais barato e {menorp}  ')