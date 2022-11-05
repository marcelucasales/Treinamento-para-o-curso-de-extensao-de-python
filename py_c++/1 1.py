l1 = float(input('Digite o valor de um lado: '))
l2 = float(input('Digite o valor de um lado: '))
l3 = float(input('Digite o valor de um lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1 and l1 > abs(l2-l3) and l2 > abs(l1-l3) and l3 > abs(l2-l1):
    print('Forma um triangulo')
    if l1==l2==l3:
        prit('Equilatero')
    elif l1==l2 or l1==l3 or l2==l3:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Nao forma um triangulo')
