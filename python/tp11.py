#questão 11
n = int(input('digite um número: '))
while True:
    if n > 10:
        n = str(n)
        num = [int(x) for x in n]
        if num == num[::-1]:
            print('palíndromo')
        else:
            print('não é palíndromo')
        break
    else:
        print('número menor ou igual a 10, digite novamente')
        n = int(input('digite um número: '))
