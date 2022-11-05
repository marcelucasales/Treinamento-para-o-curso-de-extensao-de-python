s = cont = num = 0
st = 'sim'
num = int(input('Digite um numero: '))
while st in 'sim':
    if num < 0:
        break
    s = num * cont
    print(f'{num} x {cont} = {s}')
    cont += 1
    if cont > 10:
        st = str(input('Deseja continuar? ')).strip().lower()
        if st in 'sim':
            cont = 0
            num = int(input('Digite um numero: '))
        elif st in 'nao':
            break
        elif st not in 'nao' and st not in 'sim':
            while st not in 'sim' and st not in 'nao':
                print('Comando incorreto, digite novamente!')
                st = str(input('Deseja continuar? ')).strip().lower()
                if st in 'sim':
                    cont = 0
                    num = int(input('Digite um numero: '))
                elif st in 'nao':
                    break