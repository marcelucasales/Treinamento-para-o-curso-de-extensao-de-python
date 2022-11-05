lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    st = str(input('Deseja continuar? [] Sim ou [] Nao: ')).strip().lower()[0]
    while st not in 'sn':
        print('Comando nao encontrado.')
        st = str(input('Deseja continuar? [] Sim ou [] Nao: ')).strip().lower()[0]
    if st in 'n':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(lista)
if 5 in lista:
    print(f'Valor 5 digitado {lista.count(5)} vezes')
else:
    print('Valor 5 nao esta na lista.')
    