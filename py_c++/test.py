numeros = []
maior = menor = 0
for i in range(0,5):
    numeros.append(int(input('Digite um numero: ')))
print(numeros)
for pos,i in enumerate(numeros):
    if pos == 0:
        maior = menor = i
    elif i > maior:
        maior = i
    elif i < menor:
        menor = i
print(f'Maior = {maior} na posição',end=' ')
for pos,i in enumerate(numeros):
    if i == maior:
        print('...{}'.format(pos),end=' ')
print(f'Menor = {menor} na posição', end=' ')
for pos,i in enumerate(numeros):
    if i == menor:
        print('...{}'.format(pos),end=' ')