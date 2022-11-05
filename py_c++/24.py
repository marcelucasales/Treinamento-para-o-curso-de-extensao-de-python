s = 'sim'
soma = cont = med = maior = menor = 0
while s in 'sim':
    num = int(input('Digite um num: '))
    s = str(input('Deseja Continuar Sim ou Nao: ')).strip().lower()
    if s != 'sim' and s != 'nao':
        s = str(input('''Digitou comando incorreto, digite novamente!
                    Deseja Continuar Sim ou Nao: ''')).strip().lower()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    elif cont != 1:
        if num >= maior:
            maior = num
        elif num <= menor:
            menor = num
med = soma/cont
print('Vc digitou {} numeros e a media e {}, o maior entre eles e {} e o menor entre eles {}'.format(cont,med,maior,menor))