peso = float(input('Digite o peso da 1 pessoa: '))
maior = peso
menor = peso
for i in range(2,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(i)))
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print('O menor peso e {} e o maior peso e {}'.format(menor,maior))
