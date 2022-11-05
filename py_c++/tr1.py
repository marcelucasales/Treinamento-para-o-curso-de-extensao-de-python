a = b = c = 0
while a==b or a==c or b==c:
    a = int(input('Digite um num: '))
    b = int(input('Digite um num: '))
    c = int(input('Digite um num: '))
    if(a==b or a==c or c==b):
        print('Numeros iguais, nao pode!')
if a>b and a>c:
    if(b>c):
        print(f'{a} - {b} - {c}')
    else:
        print(f'{a} - {c} - {b}')
elif b>a and b>c:
    if a>c:
        print(f'{b} - {a} - {c}')
    else:
        print(f'{b} - {c} - {a}')
else:
    if a>b:
        print(f'{c} - {a} - {b}')
    else:
        print(f'{c} - {b} - {a}')