numeros = list()
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n > numeros[-1]:
        print('Adicionado ao final da lista...')
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                print(f'Adicionado na {pos} da lista...')
                numeros.insert(pos,n)
                break
            pos += 1
print(numeros)