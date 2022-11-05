num = int(input('Digite um num: '))
s = 1
for c in range(1,(num+1)):
    s *= c
print('O fatorial de {} e {}'.format(num,s))