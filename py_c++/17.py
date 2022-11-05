from random import randint
cont = 0
x = randint(1,11)
palpite = False
while not palpite:
    c = int(input('Digite um num: '))
    cont += 1
    if c == x:
        palpite = True
    elif c < x:
        print('Digite um numero inteiro maior')
    elif c > x:
        print('Digite um num inteiro menor')
print('Acertou em {} tentativas, {} = {}'.format(cont,x,c))