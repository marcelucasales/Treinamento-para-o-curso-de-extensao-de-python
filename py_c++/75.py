tupla = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),int(input('Digite mais um valor: ')),int(input('Digite último valor: ')))
print(tupla)
print('Os valores pares foram:', end=' ')
for i in tupla:
    if i%2==0:
        print(i,end=' ')
if 3 in tupla:
    print(f'\nApareceu o valor 3 na posição {tupla.index(3) + 1}.')
else:
    print('\nO número três não foi digitado.')
print(f'Apareceu o 9, {tupla.count(9)} vezes.')