listagem = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transfridor',4.2)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:5.2f}')