numeros = list()
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        cont += 1
        if cont == 3:
            break
    else:
        print('Numeros iguais não são permitidos!')
numeros.sort(reverse=True)
print(f'O maior numero: {numeros[0]}')
print(f'O menor numero: {numeros[2]}')
print('Os numeros em ordem decrescente {}'.format(numeros))