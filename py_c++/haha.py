lista = list()
par = list()
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    st = str(input('Deseja continuar? [] Sim ou [] Nao: ')).strip().lower()[0]
    while st not in 'sn':
        print('Comando nao encontrado.')
        st = str(input('Deseja continuar? [] Sim ou [] Nao: ')).strip().lower()[0]
    if st in 'n':
        break
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista completa: {lista}')
print(f'A lista de pares: {par}')
print(f'A lista de impares: {impar}')