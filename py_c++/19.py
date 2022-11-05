c = int(input('Digite um numero: '))
a = c
b = 1
print('Calculando...{}! '.format(c))
while c > 0:
    b *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(b))