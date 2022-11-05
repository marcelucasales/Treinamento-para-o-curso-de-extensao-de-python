n = int(input('Digite um numero: '))
for i in range(0,11):
    s = n+i
    print('{} + {} = {}'.format(n,i,s))
for j in range(0,11):
    sub = n-j
    print('{} - {} = {}'.format(n,j,sub))
for k in range(0,11):
    p = n*k
    print('{} x {} = {}'.format(n,k,p))
for m in range(1,11):
    div = n/m
    print('{} / {} = {}'.format(n,m,div))