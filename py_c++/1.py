a = aux = b = 0
while a == b:
    a = int(input('Digite o valor de a: '))
    print(f'Esse é o valor de a: {a}')
    b = int(input('Digite o valor de b: '))
    print(f'Esse é o valor de b: {b}')
    if a==b:
        print('Valores Iguais não são permitidos!')
aux = a
a = b
b = aux
print(f'Esse agora que é o valor de a: {a}')
print(f'Esse agora que é o valor de b: {b}')
