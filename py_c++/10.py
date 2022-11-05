n = int(input('Digite o primeiro termo da sua pa: '))
r = int(input('Digite a razao da sua pa: '))
onze = n + 10*r
for i in range(n,onze,r):
    print(i, end=' ')
print('Acabou')