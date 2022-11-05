soma = cont = num = 0
while True:
    num = int(input('Digite um numero [ 999 para parar ]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Foi digitados {} numeros e a soma entre eles e {}'.format(cont,soma))