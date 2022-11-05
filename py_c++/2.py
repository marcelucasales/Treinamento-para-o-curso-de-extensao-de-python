a = ('Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
while True:
    n = int(input('Digite um num: '))
    if n>=1 and n<=10:
        break
    print('Tente novamente.')
print(f'Voce digitou o numero {a[n-1]}')

