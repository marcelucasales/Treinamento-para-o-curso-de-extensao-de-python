n = int(input('Digite um num: '))
cont = 0
for i in range(1,(n+1)):
    if n%i==0:
        print(i, end=' ')
        cont+=1
if cont == 2:
    print('Primo')
else:
    print('Nao e primo')