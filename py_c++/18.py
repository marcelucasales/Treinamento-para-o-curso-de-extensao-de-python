n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
c = 0
while c != 5:
    c = int(input('''Digite 1 para somar - 2 para mult - 3 para maior - 4 para ler novamente - 5 para sair
    : '''))
    if c != 4 and c != 3 and c != 2 and c != 1 and c != 5:
        c = int(input('Digite novamente: '))
    elif c == 1:
        print('A soma entre {} + {} = {}'.format(n1,n2,(n1+n2)))
    elif c == 2:
        print('o produto entre {} x {} = {}'.format(n1,n2,(n1*n2)))
    elif c == 3:
        if n1 > n2:
            print('O maior e {}'.format(n1))
        else:
            print('O maior e {}'.format(n2))
    elif c == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        #c = int(input('''Digite 1 para somar - 2 para mult - 3 para maior - 4 para ler novamente - 5 para sair
        #: '''))